# Rutas de los archivos
DATA_PATH = "data/raw/bank.csv"
MODEL_PATH = "models/model.joblib"
METRICS_PATH = "models/metrics.json"

# Columnas del dataset que usaremos (Features = X, Target = y)
FEATURES = ["age", "balance", "duration", "campaign"]
TARGET = "y"

# Configuración del modelo y MLOps exigida en clase
TEST_SIZE = 0.2
RANDOM_STATE = 42 # Semilla para que los resultados sean repetibles
MIN_ACCURACY = 0.70 # Puerta de calidad: si el modelo es peor que 70%, no se guarda

# Parámetros del modelo (Random Forest)
MODEL_PARAMS = {
    "n_estimators": 100,
    "max_depth": 5,
    "random_state": RANDOM_STATE
}