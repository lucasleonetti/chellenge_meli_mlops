import pandas as pd
import joblib
import os
from app import HouseFeatures  # validación de Pydantic si es necesario

# CONFIGURACIÓN
MODEL_PATH = 'models/model.pkl'

# Simulamos un archivo de nuevos datos
INPUT_DATA = [
    {
        "bedrooms": 3, "bathrooms": 1.0, "sqft_living": 1180, "sqft_lot": 5650,
        "floors": 1.0, "waterfront": 0, "view": 0
    },
    {
        "bedrooms": 4, "bathrooms": 2.5, "sqft_living": 3000, "sqft_lot": 10000,
        "floors": 2.0, "waterfront": 1, "view": 4 
    }
]
def predict_batch():
    print(f"🚀 Iniciando Inferencia Batch...")
    
    # 1. Cargar Modelo
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"No se encontró el modelo en {MODEL_PATH}")
    
    print(f"📂 Cargando modelo desde {MODEL_PATH}...")
    model = joblib.load(MODEL_PATH)
    
    # 2. Cargar Datos
    # En un caso real: df = pd.read_csv('data/new_data.csv')
    print(f"📊 Procesando {len(INPUT_DATA)} casas...")
    df = pd.DataFrame(INPUT_DATA)
    
    # 3. Predecir
    predictions = model.predict(df)
    
    # 4. Mostrar/Guardar Resultados
    df['predicted_price'] = predictions
    
    print("\n✅ Resultados:")
    print(df[['sqft_living', 'waterfront', 'view', 'predicted_price']])
    
    # Opcional: Guardar a CSV
    # df.to_csv('data/predictions.csv', index=False)

if __name__ == "__main__":
    predict_batch()