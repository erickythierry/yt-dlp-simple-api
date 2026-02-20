import json
from pathlib import Path

from yt_dlp import YoutubeDL

URL = "https://www.youtube.com/watch?v=jjnt-KS0ozE"
OUTPUT_JSON = Path(__file__).parent / "formats_disponiveis.json"

with YoutubeDL() as ydl:
    info = ydl.extract_info(URL, download=False)
    formats = info.get("formats", [])

# Estrutura só com campos úteis de cada formato
dados = {
    "url": URL,
    "titulo": info.get("title"),
    "id": info.get("id"),
    "formatos": [
        {
            "format_id": f.get("format_id"),
            "ext": f.get("ext"),
            "resolucao": f.get("height"),
            "largura": f.get("width"),
            "fps": f.get("fps"),
            "vcodec": f.get("vcodec"),
            "acodec": f.get("acodec"),
            "tamanho_aprox_mb": round(f.get("filesize", 0) / (1024 * 1024), 2) if f.get("filesize") else None,
            "nota": f.get("format_note"),
        }
        for f in formats
    ],
}

with open(OUTPUT_JSON, "w", encoding="utf-8") as arq:
    json.dump(dados, arq, ensure_ascii=False, indent=2)

print(f"Salvo em: {OUTPUT_JSON}")
