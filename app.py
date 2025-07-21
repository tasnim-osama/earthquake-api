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
