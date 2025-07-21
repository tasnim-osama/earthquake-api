import pandas as pd

# تحميل البيانات
df = pd.read_csv("jordan_earthquakes_2015_2025.csv")
df['time'] = pd.to_datetime(df['time'])

# فلترة الأردن
df = df[(df['latitude'] >= 29) & (df['latitude'] <= 33) &
        (df['longitude'] >= 34.8) & (df['longitude'] <= 36.1)]

# إضافة العمود الهدف
df['strong'] = (df['mag'] >= 4.0).astype(int)

# استخراج التاريخ
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['day'] = df['time'].dt.day

# حفظ الملف النهائي
df[['time', 'year', 'month', 'day', 'latitude', 'longitude', 'depth', 'mag', 'strong']].to_csv("earthquakes_jordan_prepared.csv", index=False)

print("✔️ تم تجهيز البيانات.")
