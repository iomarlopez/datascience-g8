import joblib
import json
from src.banco_mlops.config import MODEL_PATH, METRICS_PATH

# Cargar el modelo entrenado
model = joblib.load(MODEL_PATH)

def predict_subscription(features_dict):
    """Realiza una predicción usando el modelo entrenado."""
    # Convertir los datos a la lista que espera la IA
    features = [[
        features_dict["age"],
        features_dict["balance"],
        features_dict["duration"],
        features_dict["campaign"]
    ]]
    
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    
    return {
        "prediction": int(prediction),
        "probability_0": probabilities[0],
        "probability_1": probabilities[1]
    }

def get_model_info():
    """Lee y devuelve la ficha técnica (metrics.json)."""
    with open(METRICS_PATH, "r") as f:
        return json.load(f)