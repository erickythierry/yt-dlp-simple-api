FROM python:3.10-slim
WORKDIR /app
RUN apt update && apt install ffmpeg -y
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]
