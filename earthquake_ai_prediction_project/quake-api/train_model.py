import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# تحميل البيانات
df = pd.read_csv("earthquakes_jordan_prepared.csv")

# الميزات والهدف
X = df[['latitude', 'longitude', 'depth']]
y = df['strong']

# تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# تدريب النموذج
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# حفظ النموذج
joblib.dump(model, "earthquake_model.pkl")
print("✔️ تم تدريب النموذج وحفظه.")
