import streamlit as st
import requests

# SAME feature names as in api.py
FEATURES = ['Temperature', ' RH', ' Ws', 'Rain ', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI']

API_URL = "http://127.0.0.1:8000/api/predict"

st.title("Fire Weather Index Predictor (FastAPI Powered)")

input_data = {}
for feat in FEATURES:
    input_data[feat] = st.number_input(feat, value=0.0)

if st.button("Predict"):
    response = requests.post(API_URL, json=input_data)

    st.write("Status:", response.status_code)
    st.write("Raw response:", response.text)

    if response.status_code == 200:
        try:
            result = response.json()
            if "predicted_FWI" in result:
                st.success(f"Predicted FWI: {result['predicted_FWI']}")
            else:
                st.error(result.get("error", "Unknown error"))
        except:
            st.error("Invalid JSON returned from API")
    else:
        st.error("API Server Error")
