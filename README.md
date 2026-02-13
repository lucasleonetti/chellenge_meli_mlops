# 🏠 MLOps Challenge - House Price Prediction

Solución para el desafío técnico de MLOps, implementando una API productiva para la predicción de precios de viviendas.

## 📋 Descripción
Este proyecto replica la funcionalidad de predicción de precios del challenge propuesto, pero refactorizado bajo estándares de **MLOps** e **Ingeniería de Software**:
- **Modularidad:** Separación clara entre entrenamiento (`train.py`), inferencia (`app.py`) y configuración.
- **Robustez:** Validación de datos estricta con **Pydantic**.
- **Escalabilidad:** Contenerización optimizada con **Docker**.
- **Calidad:** Tests automatizados y pipeline de CI/CD.

## 🛠️ Stack Tecnológico
- **Python 3.11**
- **FastAPI** (API REST de alto rendimiento)
- **Scikit-Learn** (Random Forest Regressor)
- **Docker** (Multi-stage builds)
- **GitHub Actions** (CI/CD)

## 🚀 Cómo ejecutar localmente

### 1. Prerrequisitos
Tener Python 3.11 instalado.

### 2. Instalación
```bash
pip install -r requirements.txt