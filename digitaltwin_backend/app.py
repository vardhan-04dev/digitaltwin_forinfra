from flask import Flask, jsonify
from flask_cors import CORS
import random
from twin_engine.ml_model import load_model, predict_expected
from twin_engine.state import update_state
from twin_engine.ml_model import load_model, predict_expected
from twin_engine.reasoning import run_reasoning

app = Flask(__name__)
CORS(app)

load_model("twin_engine/model.pkl")

rooms = [
    {"id": 1, "name": "Room A", "block": 1},
    {"id": 2, "name": "Room B", "block": 1},
    {"id": 3, "name": "Room C", "block": 2},
]

@app.route("/api/rooms")
def get_rooms():

    response = []

    for room in rooms:

        
        live_data = {
            "temp": random.randint(25, 40),
            "humidity":random.randint(6,10),
            "power": random.randint(150, 350),
            "crowd": random.randint(0, 1)   
        }

        
        state = update_state(room["id"], live_data)

        expected = predict_expected(state)

        risk, reasons, health = run_reasoning(state, expected)

        
        response.append({
            "id": room["id"],
            "name": room["name"],
            "block": room["block"],
            "live": live_data,
            "expected": expected,
            "risk": risk,
            "reasons": reasons,
            "health": health
        })

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
