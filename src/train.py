import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, r2_score
import joblib
import os


# Seleccionamos las columnas más impactantes para el precio
FEATURES = [
    'bedrooms', 
    'bathrooms', 
    'sqft_living', 
    'sqft_lot', 
    'floors', 
    'waterfront', 
    'view',
]
TARGET = 'price'

# Rutas
MODEL_PATH = 'src/models/model.pkl'
DATA_PATH = 'src/data/kc_house_data.csv' 

def train():
    print(f"🚀 Iniciando entrenamiento con dataset: {DATA_PATH}...")
    
    # 1. Cargar datos
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Error: No se encontró {DATA_PATH}. Descarga 'kc_house_data.csv' de Kaggle.")
    
    df = pd.read_csv(DATA_PATH)
    
    # 2. Limpieza 
    df = df.dropna(subset=FEATURES + [TARGET])
    
    print(f"📊 Registros procesados: {len(df)}")

    X = df[FEATURES]
    y = df[TARGET]
    
    # 3. Split (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 4. Entrenamiento
    print("Entrenando modelo (Regresión Lineal)...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    
    # 5. Evaluación
    predictions = model.predict(X_test)
    rmse = root_mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Resultados del Modelo:")
    print(f" - RMSE (Error Promedio): ${rmse:,.2f}")
    print(f" - R2 Score (Precisión): {r2:.4f}")
    
    # 6. Guardar el modelo
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Modelo guardado exitosamente en: {MODEL_PATH}")

if __name__ == "__main__":
    train()