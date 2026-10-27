import pandas as pd
from src.banco_mlops.config import FEATURES, TARGET, DATA_PATH

def validate_data(df):
    """Revisiones básicas de calidad exigidas por la rúbrica."""
    # 1. Revisar si hay valores vacíos en las columnas que usaremos
    if df[FEATURES + [TARGET]].isnull().any().any():
        raise ValueError("Error: Hay valores vacíos (nulos) en los datos.")
    
    # 2. Revisar que no existan edades ilógicas (cero o negativas)
    if (df["age"] <= 0).any():
        raise ValueError("Error: La edad de los clientes debe ser mayor a 0.")

def load_and_split():
    """Carga el dataset del banco, lo limpia y lo valida."""
    # El archivo bank.csv usa punto y coma (;) como separador
    df = pd.read_csv(DATA_PATH, sep=";")
    
    # El resultado del banco dice 'yes' o 'no'. Lo convertimos a 1 y 0 para el modelo.
    df[TARGET] = df[TARGET].map({'yes': 1, 'no': 0})
    
    # Ejecutamos la barrera de validación
    validate_data(df)
    
    return df