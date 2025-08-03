from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
import requests
import os
from geopy.geocoders import Nominatim  # إضافة مكتبة geopy

app = Flask(__name__)

# تحميل النموذج المدرب
model = joblib.load("earthquake_model.pkl")

# تهيئة Geopy
geolocator = Nominatim(user_agent="earthquake_prediction_app")

@app.route('/')
def home():
    return render_template('realtime.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        location_name = data.get('location')
        if not location_name:
            return jsonify({'error': 'Location name is required'}), 400

        # تحويل اسم المنطقة إلى إحداثيات (latitude, longitude)
        location = geolocator.geocode(location_name)
        if not location:
            return jsonify({'error': 'Could not find coordinates for the given location'}), 404

        # إدخال النموذج (مع عمق افتراضي)
        features = pd.DataFrame([{'latitude': location.latitude, 'longitude': location.longitude, 'depth': 10}])
        prediction = model.predict(features)
        
        return jsonify({
            'location_name': location_name,
            'prediction': int(prediction[0]),
            'coordinates': [location.longitude, location.latitude]
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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

            # تجهيز مدخلات النموذج
            features = pd.DataFrame([{'latitude': latitude, 'longitude': longitude, 'depth': depth}])
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
