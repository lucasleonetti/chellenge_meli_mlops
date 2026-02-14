import joblib
import os
from src.train import MODEL_PATH, FEATURES

def test_model_exists():
    # Verificar que el modelo se ha generado correctamente
    assert os.path.exists(MODEL_PATH), "El archivo model.pkl no se ha generado."

def test_model_input_dimension():
    model = joblib.load(MODEL_PATH)
    # número correcto de features
    assert model.n_features_in_ == len(FEATURES), f"El modelo espera {model.n_features_in_} features, pero definimos {len(FEATURES)}"