FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# dependencias del sistema necesarias (solo si hacen falta)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# código fuente
COPY src/ ./src
COPY models/ ./models

# usuario no-root (seguridad)
RUN useradd -m appuser
USER appuser

# Exponemos el puerto
EXPOSE 8000

# ejecución
CMD ["python", "src/app.py"]