import pandas as pd

# تحميل البيانات من الملف الشامل
df = pd.read_csv("earthquakes_1950_2025_combined.csv")
df['time'] = pd.to_datetime(df['time'])

# إضافة العمود الهدف
df['strong'] = (df['mag'] >= 4.0).astype(int)

# استخراج التاريخ
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['day'] = df['time'].dt.day

# حفظ الملف النهائي (يمكنك تغيير الاسم ليكون أكثر عمومية)
df[['time', 'year', 'month', 'day', 'latitude', 'longitude', 'depth', 'mag', 'strong']].to_csv("earthquakes_prepared.csv", index=False)

print("✔️ تم تجهيز البيانات.")