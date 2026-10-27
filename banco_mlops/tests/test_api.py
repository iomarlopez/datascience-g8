import sys
import os
sys.path.insert(0, os.getcwd())  # Le enseña a Python a encontrar la carpeta 'src'

from fastapi.testclient import TestClient
from src.banco_mlops.api import app

# Creamos un cliente de prueba para la API
client = TestClient(app)

def test_read_root():
    """Prueba que la ruta raíz responda correctamente."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "API del Banco funcionando correctamente"}

def test_model_info():
    """Prueba que la ficha técnica del modelo exista y responda."""
    response = client.get("/model-info")
    assert response.status_code == 200
    data = response.json()
    assert "model_type" in data
    assert data["model_type"] == "RandomForestClassifier"

def test_predict_endpoint():
    """Prueba que la API realice predicciones correctamente."""
    payload = {
        "age": 35,
        "balance": 2000.0,
        "duration": 150,
        "campaign": 1
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "prediccion" in data
    assert "probabilidad_de_certeza" in data