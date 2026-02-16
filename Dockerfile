# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Evita archivos .pyc y logs en buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias del sistema (opcional, pero buena práctica)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar TODO el código (incluyendo src/data/kc_house_data.csv que ya forzamos en git para que cuando construya la imagen lo tenga disponible)
COPY . .

# Ejecutamos el entrenamiento DENTRO de la construcción de la imagen.
# Esto genera models/model.pkl y lo deja guardado en la imagen. (para este pequenio proyecto es ideal, no para grandes modelos o datasets)
RUN python src/train.py
# --------------------------

# Crear usuario no-root (Seguridad)
RUN useradd -m appuser
USER appuser

# Exponer el puerto
EXPOSE 8080

# ejecutar la API con Uvicorn
CMD uvicorn src.app:app --host 0.0.0.0 --port 8080