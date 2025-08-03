from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import requests
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load("earthquake_model.pkl")

@app.route('/')
def home():
    return render_template('realtime.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = pd.DataFrame([data])
        prediction = model.predict(features)
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/earthquakes')
def get_earthquakes():
    try:
        url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson"
        response = requests.get(url)
        data = response.json()

        earthquakes = []
        for feature in data['features']:
            props = feature['properties']
            coords = feature['geometry']['coordinates']
            longitude, latitude, depth = coords

            # Prepare model input
            features = pd.DataFrame([{
                'latitude': latitude,
                'longitude': longitude,
                'depth': depth
            }])

            prediction = model.predict(features)[0]

            earthquake = {
                'place': props['place'],
                'magnitude': props['mag'],
                'time': props['time'],
                'coordinates': coords,
                'prediction': int(prediction)
            }
            earthquakes.append(earthquake)

        return jsonify(earthquakes)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)