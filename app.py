from flask import Flask, request, jsonify, Response
import joblib
import os

app = Flask(__name__)

@app.route('/')
def home():
    if os.path.exists("README.md"):
        with open("README.md", encoding="utf-8") as f:
            content = f.read()
        return Response(content, mimetype="text/plain")
    return "README.md not found", 404

@app.route('/predict', methods=['POST'])
def predict():
    if not os.path.exists("earthquake_model.pkl"):
        return jsonify({"error": "Model file not found."}), 500

    model = joblib.load("earthquake_model.pkl")

    data = request.get_json()
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    depth = data.get("depth")

    prediction = model.predict([[latitude, longitude, depth]])[0]
    probability = model.predict_proba([[latitude, longitude, depth]])[0][prediction]

    message = "✅ لا يُتوقع حدوث زلزال." if prediction == 0 else "⚠️ يُحتمل حدوث زلزال."
    return jsonify({
        "prediction": int(prediction),
        "probability": round(float(probability), 2),
        "message": message
    })

if __name__ == '__main__':
    app.run(debug=True)

import requests
from flask import render_template  # إذا لم يكن موجودًا

@app.route('/realtime')
def realtime_prediction():
    # جلب بيانات الزلازل الأخيرة من USGS
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",
        "starttime": "2024-07-01",
        "endtime": "2025-07-21",
        "minlatitude": 29.0,
        "maxlatitude": 33.5,
        "minlongitude": 34.0,
        "maxlongitude": 39.0,
        "minmagnitude": 2.5
    }

    response = requests.get(url, params=params)
    data = response.json()

    model = joblib.load("earthquake_model.pkl")
    predictions = []

    for quake in data["features"]:
        props = quake["properties"]
        coords = quake["geometry"]["coordinates"]

        longitude = coords[0]
        latitude = coords[1]
        depth = coords[2]

        prediction = model.predict([[latitude, longitude, depth]])[0]
        probability = model.predict_proba([[latitude, longitude, depth]])[0][prediction]

        predictions.append({
            "place": props["place"],
            "mag": props["mag"],
            "time": props["time"],
            "latitude": latitude,
            "longitude": longitude,
            "depth": depth,
            "prediction": int(prediction),
            "probability": round(float(probability), 2),
        })

    return render_template("realtime.html", predictions=predictions)
