
# Earthquake Prediction API 🇯🇴

This is a Flask-based web application that predicts the probability of earthquakes in Jordan using a machine learning model trained on historical earthquake data.

## 🔍 Features
- Trained ML model on earthquake data from 2015–2025.
- Real-time visualization from USGS (United States Geological Survey).
- API endpoint for predictions.
- Web interface for displaying current data and predictions.

## 🧠 Machine Learning
The model is trained using features like magnitude, depth, and location from CSV datasets. It outputs a probability of earthquake occurrence.

## 🚀 How to Run Locally

1. Install requirements:
   ```bash
   pip install -r requirements.txt

## 👩‍💻 Developed by
**Tasnim Al-Hanini**  
[GitHub Profile](https://github.com/tasnim-osama)




# earthquake-api
# 🌍 Earthquake Prediction API – تنبؤ الزلازل في الأردن باستخدام الذكاء الاصطناعي

نظام تنبؤ زلازل مبني على تقنيات تعلم الآلة (Machine Learning)، تم تطويره باستخدام لغة Python ومكتبة Flask لإنشاء واجهة برمجية (API).  
يعتمد المشروع على بيانات زلازل حقيقية من الأردن بين عامي 2015 و2025.

---

## 📌 المميزات

- 🔮 التنبؤ باحتمالية وقوع زلزال بناءً على الموقع الجغرافي والعمق.
- 🧠 تدريب نموذج Random Forest باستخدام بيانات CSV.
- 🧪 اختبار النموذج محليًا.
- ☁️ قابل للنشر تلقائي على Render.
- 📡 واجهة API بسيطة وسهلة الاستخدام.

---

## 🗂️ بنية المشروع

📦 earthquake-ai-prediction
├── app.py ← تطبيق Flask
├── prepare_data.py ← تجهيز البيانات
├── train_model.py ← تدريب النموذج
├── predict_quake.py ← اختبار التنبؤ
├── requirements.txt ← مكتبات Python المطلوبة
├── render.yaml ← إعداد نشر على Render
├── earthquakes_jordan_prepared.csv ← بيانات جاهزة للتدريب
├── jordan_earthquakes_2015_2025.csv ← بيانات خام
└── README.md


👩‍💻 المطورة
Tasnim Osama
🔗 GitHub: @tasnim-osama
