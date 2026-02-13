# twin_logic/reasoning.py

def run_reasoning(state, expected):

    real_temp = state["temp"]
    real_power = state["power"]
    real_crowd = state["crowd"]

    temp_error = (real_temp - expected["temp"])
    power_error = (real_power - expected["power"])
    crowd_error = (real_crowd - expected["crowd"])

    risk_score = 0
    reasons = []

    if temp_error > 3:
        risk_score += 2
        reasons.append(
            "Thermal rise diverging from learned 2-minute behaviour trajectory"
        )

    if power_error > 20:
        risk_score += 2
        reasons.append(
            "Energy consumption deviating from predicted operational load profile"
        )

    if crowd_error > 0:
        risk_score += 1
        reasons.append(
            "PIR activity inconsistent with expected occupancy rhythm"
        )

    if temp_error > 3 and power_error < 10:
        reasons.append(
            "Heat accumulation detected without proportional energy input"
        )

    if power_error > 20 and real_crowd == 0:
        reasons.append(
            "Energy spike detected during low occupancy window"
        )

    state["health"] -= (risk_score)*0.6
    state["health"] = max(0, min(100, state["health"]))

    # risk level
    if risk_score >= 4:
        risk = "HIGH"
    elif risk_score >= 2:
        risk = "MEDIUM"
    else:
        risk = "NORMAL"

    return risk, reasons, state["health"]
