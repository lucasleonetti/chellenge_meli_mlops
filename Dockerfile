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

# Copiar TODO el código (incluyendo src/data/kc_house_data.csv que ya forzamos en git)
COPY . .

# --- LA SOLUCIÓN MÁGICA ---
# Ejecutamos el entrenamiento DENTRO de la construcción de la imagen.
# Esto genera models/model.pkl y lo deja guardado en la imagen.
RUN python src/train.py
# --------------------------

# Crear usuario no-root (Seguridad)
RUN useradd -m appuser
USER appuser

# Exponer el puerto
EXPOSE 8080

# Comando de inicio usando la variable de entorno PORT (Cloud Run friendly)
# Usamos shell form (sh -c) para que lea la variable $PORT correctamente
CMD uvicorn src.app:app --host 0.0.0.0 --port 8080