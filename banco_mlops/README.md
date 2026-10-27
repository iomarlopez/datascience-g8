# 🏦 Proyecto Final MLOps - Bank Marketing

Proyecto final de Machine Learning Operations (MLOps), basado en el dataset *Bank Marketing* de UCI.

## 📁 Estructura del Proyecto
- `app/`: Contiene la interfaz web interactiva desarrollada con **Streamlit**.
- `data/`: Almacena el dataset original (`bank.csv` en `data/raw/`).
- `models/`: Archivos generados automáticamente tras el entrenamiento (`model.joblib` y la ficha técnica `metrics.json`).
- `src/banco_mlops/`: Código fuente principal del proyecto:
  - `config.py`: Parámetros y rutas globales.
  - `data.py`: Carga y validación de calidad de datos.
  - `train.py`: Script de entrenamiento del modelo (Random Forest) con puerta de calidad.
  - `predict.py`: Funciones de inferencia basadas en el modelo guardado.
  - `api.py`: API backend desarrollada con **FastAPI** y validación de esquemas con **Pydantic**.
- `tests/`: Pruebas automáticas de la API implementadas con **pytest**.

---

## 🚀 Guía de Ejecución Local

Asegúrate de tener instalado **Python 3.11** y el gestor de paquetes **`uv`**.
### 1. Entrenar el modelo
Ejecuta el script de entrenamiento para generar el modelo y su ficha técnica en la carpeta `models/`:
```powershell
uv run python -m src.banco_mlops.train
```

### 2. Ejecutar la API (Backend)
Enciende el servidor con FastAPI:
```powershell
uv run fastapi dev src/banco_mlops/api.py
```
*La documentación interactiva estará disponible en:* `http://127.0.0.1:8000/docs`

### 3. Ejecutar la Interfaz Web (Frontend)
Abre una **nueva terminal** y lanza la aplicación de Streamlit:
```powershell
uv run streamlit run app/streamlit_app.py
```

### 4. Ejecutar las Pruebas Automáticas
Para verificar que todas las pruebas pasen correctamente:
```powershell
uv run pytest -v
```