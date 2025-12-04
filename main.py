import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/api/predict"

st.set_page_config(page_title="FWI Prediction", page_icon="🔥", layout="centered")

st.title("🔥 Fire Weather Index (FWI) Prediction")
st.markdown("Enter the meteorological parameters below to get the predicted FWI value.")

# Input columns
col1, col2 = st.columns(2)

with col1:
    day = st.number_input("Day", min_value=1, max_value=31, value=15)
    month = st.number_input("Month", min_value=1, max_value=12, value=7)
    year = st.number_input("Year", min_value=1900, max_value=2100, value=2012)
    Temperature = st.number_input("Temperature (°C)", value=30.0)
    RH = st.number_input("Relative Humidity (%)", value=40.0)
    WS = st.number_input("Wind Speed (km/h)", value=6.0)

with col2:
    Rain = st.number_input("Rain (mm)", value=0.0)
    FFMC = st.number_input("FFMC", value=85.0)
    DMC = st.number_input("DMC", value=25.0)
    DC = st.number_input("DC", value=60.0)
    ISI = st.number_input("ISI", value=5.0)
    BUI = st.number_input("BUI", value=30.0)

# Predict button
if st.button("🔥 Predict FWI"):
    data = {
        "Day": day,
        "Month": month,
        "Year": year,
        "Temperature": Temperature,
        "RH": RH,
        "WS": WS,
        "Rain": Rain,
        "FFMC": FFMC,
        "DMC": DMC,
        "DC": DC,
        "ISI": ISI,
        "BUI": BUI
    }

    response = requests.post(API_URL, json=data)

    try:
        result = response.json()
        st.success(f"Predicted FWI: **{result['predicted_FWI']}**")
    except:
        st.error("Error occurred. Check backend connection.")
