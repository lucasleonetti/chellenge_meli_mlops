from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import os

# Inicializar la app
app = FastAPI(
    title="King County House Price API", 
    description="API para predecir precios de casas en Seattle (King County) usando Regresión Lineal.",
    version="1.0.0"
)

# Cargar el modelo al inicio (Cold Start)
MODEL_PATH = 'src/models/model.pkl'

# Verificación de seguridad: El modelo debe existir
if not os.path.exists(MODEL_PATH):
    # En un entorno real, esto podría bajar el modelo de S3/GCS si no está local
    raise RuntimeError(f"CRITICAL: No se encontró el modelo en {MODEL_PATH}. Ejecuta src/train.py primero.")

model = joblib.load(MODEL_PATH)

# Definir el esquema de entrada (INPUT SCHEMA) basado en King County
class HouseFeatures(BaseModel):
    bedrooms: int = Field(..., ge=0, description="Número de habitaciones")
    bathrooms: float = Field(..., ge=0, description="Número de baños (puede ser decimal, ej. 2.5)")
    sqft_living: int = Field(..., ge=0, description="Pies cuadrados de espacio habitable")
    sqft_lot: int = Field(..., ge=0, description="Pies cuadrados del terreno")
    floors: float = Field(..., ge=0, description="Número de pisos")
    waterfront: int = Field(0, ge=0, le=1, description="1 si tiene vista al agua, 0 si no")
    view: int = Field(0, ge=0, le=4, description="Calidad de la vista (0-4)")

    # Ejemplo para la documentación automática (Swagger UI)
    class Config:
        json_schema_extra = {
            "example": {
                "bedrooms": 3,
                "bathrooms": 2.5,
                "sqft_living": 2500,
                "sqft_lot": 7242,
                "floors": 2.0,
                "waterfront": 0,
                "view": 0,
            }
        }

@app.get("/")
def health_check():
    return {"status": "ok", "message": "ML Service is ready for inference"}

@app.post("/predict")
def predict_price(features: HouseFeatures):
    try:
        # Convertir datos a DataFrame (el formato que espera sklearn)
        # Usamos .model_dump() para Pydantic v2
        data_df = pd.DataFrame([features.model_dump()])
        
        # Realizar predicción
        prediction = model.predict(data_df)
        
        return {
            "predicted_price": round(float(prediction[0]), 2),
            "currency": "USD",
            "model_version": "v1.0.0"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction Error: {str(e)}")