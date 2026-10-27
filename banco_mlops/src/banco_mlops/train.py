import json
import joblib
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.banco_mlops.data import load_and_split
from src.banco_mlops.config import (FEATURES, TARGET, TEST_SIZE, RANDOM_STATE, 
                                    MODEL_PARAMS, MIN_ACCURACY, MODEL_PATH, METRICS_PATH)

def run_training():
    print("1) Cargando datos...")
    df = load_and_split()
    X = df[FEATURES]
    y = df[TARGET]
    
    print("2) Separando datos para entrenamiento y prueba...")
    # stratify=y asegura que ambos grupos tengan la misma proporción de respuestas 'yes' y 'no'
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
    )
    
    print("3) Entrenando el modelo RandomForest...")
    model = RandomForestClassifier(**MODEL_PARAMS)
    model.fit(X_train, y_train)
    
    print("4) Evaluando el modelo...")
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"   Accuracy obtenido: {accuracy:.4f}")
    
    # Puerta de calidad
    if accuracy < MIN_ACCURACY:
        raise SystemExit(f"El modelo no supera el mínimo de {MIN_ACCURACY}. No se guardará.")
        
    print("5) Guardando modelo y ficha técnica...")
    metrics = {
        "model_version": "1.0.0",
        "trained_at": datetime.now().isoformat(),
        "model_type": "RandomForestClassifier",
        "params": MODEL_PARAMS,
        "accuracy": accuracy
    }
    
    joblib.dump(model, MODEL_PATH)
    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=4)
        
    print("¡Entrenamiento finalizado con éxito!")

if __name__ == "__main__":
    run_training()