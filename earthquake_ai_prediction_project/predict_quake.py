import pandas as pd
import joblib

# تحميل النموذج
model = joblib.load("earthquake_model.pkl")

# مثال لقيم زلزالية جديدة
sample = pd.DataFrame([{
    'latitude': 31.5,
    'longitude': 35.6,
    'depth': 12
}])

# التنبؤ
prediction = model.predict(sample)[0]
proba = model.predict_proba(sample)[0][1]

if prediction == 1:
    print(f"⚠️ من المتوقع حدوث زلزال! النسبة: {proba:.2%}")
else:
    print(f"✅ لا يُتوقع حدوث زلزال. النسبة: {proba:.2%}")
