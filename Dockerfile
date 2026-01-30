FROM python:3.10-slim

WORKDIR /app

# Instalar dependências necessárias para o Deno + ffmpeg
RUN apt update && apt install -y \
    ffmpeg \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Instalar Deno via script oficial
RUN curl -fsSL https://deno.land/install.sh | sh

# Adicionar o Deno ao PATH
ENV DENO_INSTALL=/root/.deno
ENV PATH="${DENO_INSTALL}/bin:${PATH}"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 5000

# CMD ["python", "main.py"]
CMD ["sh", "start.sh"]