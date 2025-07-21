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
