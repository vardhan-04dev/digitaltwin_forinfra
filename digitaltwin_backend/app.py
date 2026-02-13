from flask import Flask, jsonify
from flask_cors import CORS
import random

from twin_engine.state import update_state
from twin_engine.ml_model import load_model, predict_expected
from twin_engine.reasoning import run_reasoning

app = Flask(__name__)
CORS(app)

# load ML model once when server starts
load_model("model.pkl")

rooms = [
    {"id": 1, "name": "Room A", "floor": 1},
    {"id": 2, "name": "Room B", "floor": 1},
    {"id": 3, "name": "Room C", "floor": 2},
]

@app.route("/api/rooms")
def get_rooms():

    response = []

    for room in rooms:

        # ---- fake live sensor data (replace with firebase later) ----
        live_data = {
            "temp": random.randint(25, 40),
            "power": random.randint(150, 350),
            "crowd": random.randint(0, 1)   # PIR output
        }

        
        state = update_state(room["id"], live_data)

        expected = predict_expected(state)

        risk, reasons, health = run_reasoning(state, expected)

        
        response.append({
            "id": room["id"],
            "name": room["name"],
            "floor": room["floor"],
            "live": live_data,
            "expected": expected,
            "risk": risk,
            "reasons": reasons,
            "health": health
        })

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
