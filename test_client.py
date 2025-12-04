import requests

url = "http://localhost:5000/predict"
data = {
    "Temperature": 30,
    "RH": 45,
    "Ws": 20,
    "Rain": 0.0,
    "FFMC": 85.0,
    "DMC": 26.2,
    "DC": 94.3,
    "ISI": 5.4,
    "BUI": 66.0,
    "FWI": 10.1
}

response = requests.post(url, json=data)
print(response.json())
