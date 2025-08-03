
import pandas as pd

# تحميل البيانات الخام الجديدة لجميع المناطق
# هذا الملف يحتوي على بيانات من 1950 إلى 2025
df = pd.read_csv("earthquakes_1950_2025_combined.csv")

# تحويل عمود الوقت إلى صيغة datetime
df['time'] = pd.to_datetime(df['time'])

# إضافة العمود الهدف 'strong' بناءً على القوة (mag)
# الزلزال يعتبر "قويًا" إذا كانت قوته 4.0 أو أكثر
df['strong'] = (df['mag'] >= 4.0).astype(int)

# استخراج التاريخ
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['day'] = df['time'].dt.day

# حفظ الملف النهائي
# سيتم حفظه بنفس الاسم لكي لا تحتاج الملفات الأخرى للتعديل
df[['time', 'year', 'month', 'day', 'latitude', 'longitude', 'depth', 'mag', 'strong']].to_csv("earthquakes_jordan_prepared.csv", index=False)

print("✔️ تم تجهيز البيانات الجديدة لجميع المناطق وحفظها في earthquakes_jordan_prepared.csv.")

