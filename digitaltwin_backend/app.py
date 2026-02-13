from flask import Flask, jsonify
from flask_cors import CORS
import random



app = Flask(__name__)
CORS(app)


rooms = [
    {"id": 1, "name": "Room A", "floor": 1},
    {"id": 2, "name": "Room B", "floor": 1},
    {"id": 3, "name": "Room C", "floor": 2},
]

@app.route("/api/rooms")
def get_rooms():

    response = []

    for room in rooms:

        live_data = {
            "temp": random.randint(25, 40),
            "humidity": random.randint(30, 70),
            "power": random.randint(150, 350),
            "crowd": random.randint(0, 1)   
        }

        
        response.append({
            "id": room["id"],
            "name": room["name"],
            "floor": room["floor"],
            "live": live_data,
        })

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
