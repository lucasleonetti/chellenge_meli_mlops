# Descripcion

Este proyecto es una implementación de un modelo de Machine Learning para predecir precios de viviendas utilizando el dataset "kc_house_data.csv". El modelo se entrena con una Regresión Lineal Simple y se expone a través de una API RESTful construida con FastAPI. El proyecto está diseñado para ser desplegado en Google Cloud Run, utilizando Docker para la contenedorización y DVC para el versionado de datos.

## 🛠️ Stack Tecnológico

Lenguaje: Python 3.11 (Slim version para optimizar imágenes).

API Framework: FastAPI (Validación de datos nativa con Pydantic).

Machine Learning: Scikit-Learn (Linear Regression Simple).

Contenedores: Docker (Multi-stage builds & Rootless security).

Infraestructura: Google Cloud Run + Artifact Registry.

CI/CD: GitHub Actions.

Gobierno de Datos: DVC (Data Version Control) implementado para trazabilidad.

### 📋 Estructura del Proyecto

La estructura está diseñada para separar responsabilidades entre entrenamiento, inferencia y configuración.

### 🚀 Guía de Ejecución Local

Sigue estos pasos para levantar el proyecto en tu máquina.

1. Prerrequisitos

   - Python 3.11
   - Git

2. Instalación de Dependencias

3. Entrenar el Modelo
Este script procesa el dataset kc_house_data.csv, entrena una Regresión Lineal y guarda el artefacto en models/model.pkl.
    - Output esperado: ✅ Modelo guardado exitosamente en: models/model.pkl
4. Levantar la API
Inicia el servidor de desarrollo local.

La API estará disponible en: http://127.0.0.1:8000

### 🐳 Ejecución con Docker

Para simular el entorno productivo exacto, utiliza Docker.

### 🧪 Testing y Calidad

El proyecto incluye tests automatizados para validar tanto la disponibilidad de la API como la integridad del modelo.

### ☁️ Despliegue en Producción

La aplicación se encuentra desplegada y operativa en Google Cloud Run.

    - URL del Servicio: https://mlops-meli-1091336880261.us-south1.run.app/

    - Documentación Interactiva (Swagger): https://mlops-meli-1091336880261.us-south1.run.app/docs

Puedes probar el endpoint /predict enviando el siguiente JSON:

### 🛡️Notas de Seguridad y MLOps

    - DVC: Se utiliza DVC para el versionado de datos. Nota: Para facilitar la evaluación de este challenge, el dataset .csv se ha incluido en el repositorio git, aunque en un entorno real residiría exclusivamente en un bucket de almacenamiento.

    - Secretos: Las credenciales de GCP se gestionan mediante GitHub Secrets y no están expuestas en el código.

    - Usuario no-root: El Dockerfile configura un usuario appuser para mitigar riesgos de seguridad en el contenedor.

### Autor: Lucas Leonetti
