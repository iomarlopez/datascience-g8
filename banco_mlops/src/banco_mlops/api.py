import sys
import os
sys.path.insert(0, os.getcwd())  # Le enseña a Python a encontrar la carpeta 'src'

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.banco_mlops.predict import predict_subscription, get_model_info

app = FastAPI(title="API Bank Marketing MLOps")

# Validación de entrada con Pydantic (Requisito de la rúbrica)
class ClientInput(BaseModel):
    age: int = Field(gt=0, description="Edad del cliente")
    balance: float = Field(description="Saldo promedio anual")
    duration: float = Field(gt=0, description="Duración del contacto")
    campaign: int = Field(gt=0, description="Número de contactos")

@app.get("/")
def read_root():
    return {"status": "API del Banco funcionando correctamente"}

@app.get("/model-info")
def model_info():
    """Devuelve la ficha técnica del modelo."""
    try:
        return get_model_info()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Ficha técnica no encontrada.")

@app.post("/predict")
def predict(client: ClientInput):
    """Recibe datos de un cliente y predice si aceptará el depósito."""
    result = predict_subscription(client.model_dump())
    
    respuesta = "Si aceptara" if result["prediction"] == 1 else "No aceptara"
    probabilidad = result["probability_1"] if result["prediction"] == 1 else result["probability_0"]
    
    return {
        "prediccion": respuesta,
        "probabilidad_de_certeza": round(float(probabilidad) * 100, 2)
    }