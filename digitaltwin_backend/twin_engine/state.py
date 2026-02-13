room_states = {}

def get_room_state(room_id):
    if room_id not in room_states:
        room_states[room_id] = {
            "temp": 0,
            "humidity":0,
            "power": 0,
            "crowd": 0,
            "health": 100,
            "temp_history": [],
            "humidity_history": [],
            "pow_history": [],
            "crowd_history": []
        }
    return room_states[room_id]


def update_state(room_id, live_data):

    state = get_room_state(room_id)

    state["temp"] = live_data["temp"]
    state["humidity"] = live_data["humidity"]
    state["power"] = live_data["power"]
    state["crowd"] = live_data["crowd"]

    state["temp_history"].append(live_data["temp"])
    state["humidity_history"].append(live_data["temp"])
    state["pow_history"].append(live_data["power"])
    state["crowd_history"].append(live_data["crowd"])

    if len(state["temp_history"]) > 50:
        state["temp_history"].pop(0)

    if len(state["pow_history"]) > 50:
        state["pow_history"].pop(0)

    if len(state["crowd_history"]) > 50:
        state["crowd_history"].pop(0)

    if len(state["crowd_history"]) > 50:
        state["crowd_history"].pop(0)

    return state
