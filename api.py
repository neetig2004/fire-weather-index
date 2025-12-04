from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI(title="FWI Prediction API")

# Allow all origins (so Streamlit can call the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model (your model.pkl is ONLY the model object)
model = joblib.load("model.pkl")

# IMPORTANT: feature names must match training EXACTLY (with spaces)
features = ['Temperature', ' RH', ' Ws', 'Rain ', 'FFMC', 'DMC', 'DC', 'ISI', 'BUI']


@app.get("/")
def home():
    return {"message": "Welcome to the Fire Weather Index Prediction API!"}


@app.post("/api/predict")
def predict(data: dict):
    """
    Expect JSON like:
    {
        "Temperature": 25,
        " RH": 40,
        " Ws": 10,
        "Rain ": 0,
        "FFMC": 85,
        "DMC": 50,
        "DC": 100,
        "ISI": 7,
        "BUI": 60
    }
    """
    try:
        # Arrange input values in the correct order
        input_values = [[data[f] for f in features]]
        df_input = pd.DataFrame(input_values, columns=features)

        pred = round(float(model.predict(df_input)[0]), 3)

        return {"predicted_FWI": pred}

    except Exception as e:
        return {"error": str(e)}
