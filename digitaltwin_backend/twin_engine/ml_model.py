import numpy as np
import joblib

model = None

def load_model(path="model.pkl"):
    global model
    model = joblib.load(path)

def predict_expected(state):

    if model is None:
        raise ValueError("model is not loaded")

    features = np.array([[
        state["temp"],
        state["humidity"],
        state["power"],
        state["crowd"]
    ]])

    prediction = model.predict(features)[0]

    return {
        "temp": prediction[0],
        "humidity":prediction[1],
        "power": prediction[2],
        "crowd": prediction[3]
    }
