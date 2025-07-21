from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# تحميل النموذج
model = joblib.load("earthquake_model.pkl")

@app.route('/')
def home():
    return "🚨 Earthquake Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # التأكد من وجود الحقول المطلوبة
    required = ['latitude', 'longitude', 'depth']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing data. Required: latitude, longitude, depth'}), 400

    # تحويل البيانات إلى DataFrame
    sample = pd.DataFrame([{
        'latitude': data['latitude'],
        'longitude': data['longitude'],
        'depth': data['depth']
    }])

    # التنبؤ
    prediction = model.predict(sample)[0]
    proba = model.predict_proba(sample)[0][1]

    # إعداد النتيجة
    result = {
        'prediction': int(prediction),
        'probability': round(proba, 4),
        'message': "⚠️ من المتوقع حدوث زلزال!" if prediction == 1 else "✅ لا يُتوقع حدوث زلزال."
    }

    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False, host='0.0.0.0', port=port)
