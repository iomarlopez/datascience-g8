import streamlit as st
import requests

st.set_page_config(page_title="Bank Marketing MLOps", layout="centered")

st.title("🏦 Predicción de Depósito Bancario")
st.write("Ingresa los datos del cliente para predecir si aceptará la campaña del banco.")

# Controles de la interfaz
age = st.number_input("Edad del cliente", min_value=18, max_value=100, value=30)
balance = st.number_input("Saldo promedio anual (€)", value=1500.0)
duration = st.number_input("Duración de la última llamada (segundos)", min_value=1, value=120)
campaign = st.number_input("Número de contactos en esta campaña", min_value=1, value=2)

if st.button("Consultar a la API"):
    # URL de nuestra API local
    api_url = "http://127.0.0.1:8000/predict"
    
    # Datos que enviaremos a la API
    payload = {
        "age": age,
        "balance": balance,
        "duration": duration,
        "campaign": campaign
    }
    
    try:
        # Hacemos la petición POST a FastAPI
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            if result["prediccion"] == "Si aceptara":
                st.success(f"✅ ¡El cliente SÍ aceptará! (Probabilidad: {result['probabilidad_de_certeza']}%)")
            else:
                st.error(f"❌ El cliente NO aceptará. (Probabilidad de rechazo: {result['probabilidad_de_certeza']}%)")
        else:
            st.warning("Error en la respuesta de la API.")
    except Exception as e:
        st.error(f"Error al conectar con la API. Asegúrate de que la API esté corriendo en la otra terminal. Detalle: {e}")