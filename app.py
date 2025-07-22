from flask import Flask, request, jsonify, render_template
import joblib
import requests
import os

app = Flask(__name__)
model = joblib.load("earthquake_model.pkl")

@app.route('/')
def home():
    return render_template('realtime.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])
        depth = float(data['depth'])

        prediction = model.predict([[latitude, longitude, depth]])
        return jsonify({'prediction': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
