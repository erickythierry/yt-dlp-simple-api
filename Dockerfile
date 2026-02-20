FROM python:3.10-slim

WORKDIR /app

RUN apt update && apt install -y \
    ffmpeg \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

RUN ARCH=$(dpkg --print-architecture) && \
    case "$ARCH" in \
      amd64) DENO_ARCH="x86_64-unknown-linux-gnu" ;; \
      arm64) DENO_ARCH="aarch64-unknown-linux-gnu" ;; \
      *) echo "Arquitetura não suportada: $ARCH" && exit 1 ;; \
    esac && \
    curl -fsSL "https://github.com/denoland/deno/releases/latest/download/deno-${DENO_ARCH}.zip" \
    -o deno.zip \
    && unzip deno.zip \
    && mv deno /usr/local/bin/deno \
    && rm deno.zip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 5000

CMD ["sh", "start.sh"]