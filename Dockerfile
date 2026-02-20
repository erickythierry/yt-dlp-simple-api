# -------- STAGE 1: Deno binário oficial --------
FROM denoland/deno:bin-1.42.4 AS deno

# -------- STAGE 2: Python app --------
FROM python:3.11-slim

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive

# Dependências de sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas o binário do Deno
COPY --from=deno /deno /usr/local/bin/deno

# Garante permissão de execução
RUN chmod +x /usr/local/bin/deno && deno --version

# Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código da aplicação
COPY . .

RUN chmod +x start.sh

EXPOSE 5000

CMD ["sh", "start.sh"]