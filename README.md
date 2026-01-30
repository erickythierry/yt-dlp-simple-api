# YouTube Downloader API

Uma API RESTful simples e eficiente para download de vídeos e áudio do YouTube, construída em Python utilizando a biblioteca [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## 📋 Sobre o Projeto

Este projeto fornece uma API básica e intuitiva para fazer download de conteúdo do YouTube em diferentes formatos. Desenvolvida como alternativa ao projeto [ytdl-simple-api](https://github.com/erickythierry/ytdl-simple-api), que utilizava a biblioteca [ytdl-core](https://github.com/fent/node-ytdl-core) em Node.js com problemas de manutenção.

## 🚀 Funcionalidades

- ✅ Download de áudio em WebM
- ✅ Download de vídeo em WebM ou MP4
- ✅ Suporte a proxy SOCKS5
- ✅ Containerização com Docker
- ✅ Interface RESTful simples

## 📦 Docker

Este projeto pode ser containerizado com Docker. Para mais informações sobre como construir e executar a imagem, consulte o `Dockerfile` no repositório.

## ⚙️ Instalação e Configuração

### Instalação Local

1. Clone o repositório:

    ```bash
    git clone <repository-url>
    cd yt-dlp
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação:

    ```bash
    python main.py
    ```

    Ou no Linux:

    ```bash
    python3 main.py
    ```

A API estará disponível em `http://localhost:5000`

## 🔌 Endpoints

### Download de Áudio

```
POST /download/audio
```

Realiza download do áudio em formato WebM

### Download de Vídeo

```
POST /download/video
```

Realiza download do vídeo em formato WebM ou MP4

## 📝 Exemplos de Uso

### Com cURL

**Download de áudio:**

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"url": "LINK_VIDEO"}' \
  http://localhost:5000/download/audio \
  -O
```

**Download de vídeo:**

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"url": "LINK_VIDEO"}' \
  http://localhost:5000/download/video \
  -O
```

## 🔒 Configuração com Proxy SOCKS5

Para usar a API através de um proxy SOCKS5, crie um arquivo `.env` na raiz do projeto:

```env
PROXY="socks5://usuario:senha@IP-DO-PROXY:PORTA"
```

Alternativamente, passe a variável de ambiente ao criar o container Docker:

```bash
docker run -e PROXY="socks5://usuario:senha@IP-DO-PROXY:PORTA" rickhdamas/ytdlp-api
```
