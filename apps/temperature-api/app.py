import random
from flask import Flask, jsonify, request 
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200


@app.route("/temperature/<sensor_id>", methods=["GET"])
def get_temperature(sensor_id):
    app.logger.warning("REQUEST path=%s sensor_id=%s args=%s", request.path, sensor_id, dict(request.args))

    if sensor_id == "1":
        location = "Living Room"
    elif sensor_id == "2":
        location = "Bedroom"
    elif sensor_id == "3":
        location = "Kitchen"
    else:
        location = "Unknown"

    value = round(random.uniform(18.0, 26.0), 1)

    resp = {
        "sensorId": sensor_id,
        "location": location,
        "value": value,
        "status": "OK",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    app.logger.warning("RESPONSE %s", resp)

    return jsonify(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
