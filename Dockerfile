FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# dependencias del sistema necesarias (en el caso de necesitar compilar algo o usar ciertas librerías)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# requirements & dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# código fuente
COPY src/ ./src

# usuario no-root (seguridad)
RUN useradd -m appuser
USER appuser

# Exposicion del puerto
EXPOSE 8000

# ejecución
CMD ["python", "src/app.py"]