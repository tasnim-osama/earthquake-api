from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import requests

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
            properties = feature['properties']
            geometry = feature['geometry']
            earthquake = {
                'place': properties['place'],
                'magnitude': properties['mag'],
                'time': properties['time'],
                'coordinates': geometry['coordinates']
            }
            earthquakes.append(earthquake)

        return jsonify(earthquakes)
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
