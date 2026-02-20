from flask import Flask, request, jsonify, send_from_directory, url_for
import os
from yt_dlp import YoutubeDL
import time
import uuid
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
PROXY = os.getenv('PROXY')

# Garante que a pasta de downloads exista
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def clean_old_files(max_age_minutes=5):
    """
    Remove arquivos do diretório especificado que têm mais de `max_age_minutes` minutos de criação.

    Args:
        max_age_minutes (int): Tempo máximo permitido para os arquivos em minutos.
    """
    print("old_files")
    now = time.time()
    max_age_seconds = max_age_minutes * 60

    for filename in os.listdir(DOWNLOAD_DIR):
        file_path = os.path.join(DOWNLOAD_DIR, filename)

        if os.path.isfile(file_path):
            file_creation_time = os.path.getctime(file_path)
            if now - file_creation_time > max_age_seconds:
                os.remove(file_path)


def download_media(url, options):
    with YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)


@app.route('/download/audio', methods=['POST'])
def download_audio():
    clean_old_files()
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    print('/audio', url)

    try:
        # M4A qualidade média, sem ffmpeg (download direto)
        options = {
            "format": "bestaudio[ext=m4a]/bestaudio",
            "outtmpl": f"{DOWNLOAD_DIR}/{uuid.uuid4()}.%(ext)s",
            "noplaylist": True,
            "js_runtimes": {"deno": {}},
            "remote_components": ["ejs:github"],
        }

        if PROXY:
            print("usando proxy")
            options["proxy"] = PROXY

        file_path = download_media(url, options)
        file_name = os.path.basename(file_path)
        download_url = url_for("serve_file", filename=file_name, _external=True)
        return jsonify({"file": download_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/download/video', methods=['POST'])
def download_video():
    clean_old_files()
    data = request.json
    url = data.get("url")
    if not url:
        return jsonify({"error": "URL não fornecida"}), 400

    print('/video', url)

    try:
        # MP4 H264; 720p primeiro, depois 480p; merge só em último caso
        options = {
            "format": (
                "best[ext=mp4][vcodec^=avc][height=720]"
                "/best[ext=mp4][vcodec^=avc][height=480]"
                "/best[ext=mp4][vcodec^=avc]"
                # Último recurso: vídeo sem áudio + áudio separado (usa ffmpeg para merge)
                "/bestvideo[ext=mp4][vcodec^=avc][height<=720]+bestaudio[ext=m4a]"
            ),
            "merge_output_format": "mp4",
            "outtmpl": f"{DOWNLOAD_DIR}/{uuid.uuid4()}.%(ext)s",
            "noplaylist": True,
            "js_runtimes": {"deno": {}},
            "remote_components": ["ejs:github"],
        }

        if PROXY:
            print("usando proxy")
            options["proxy"] = PROXY

        file_path = download_media(url, options)
        file_name = os.path.basename(file_path)
        download_url = url_for("serve_file", filename=file_name, _external=True)
        return jsonify({"file": download_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/files/<path:filename>', methods=['GET'])
def serve_file(filename):
    clean_old_files()
    """Endpoint para servir arquivos diretamente da pasta downloads."""
    return send_from_directory(DOWNLOAD_DIR, filename)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", use_reloader=False)
