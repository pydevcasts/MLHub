
# تحلیل داده‌های فروش آیفون
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error



data = {
    "Product Name": [
        "APPLE iPhone 8 Plus (Gold, 64 GB)",
        "APPLE iPhone 8 Plus (Space Grey, 256 GB)",
        "APPLE iPhone 8 Plus (Space Grey, 256 GB)",
        "APPLE iPhone 8 (Silver, 256 GB)",
        "APPLE iPhone 8 (Silver, 256 GB)",
        "APPLE iPhone 8 Plus (Silver, 64 GB)",
        "APPLE iPhone 8 Plus (Space Grey, 64 GB)",
        "APPLE iPhone 8 (Space Grey, 256 GB)",
        "APPLE iPhone XS Max (Silver, 64 GB)"
    ],
    "Sale Price": [
        49900.0,
        84900.0,
        84900.0,
        77000.0,
        77000.0,
        None,
        49900.0,
        77000.0,
        89900.0
    ],
    "Mrp": [
        49900.0,
        1.0,
        84900.0,
        77000.0,
        77000.0,
        49900.0,
        None,
        77000.0,
        89900.0
    ],
    "Number Of Ratings": [
        3431,
        3431,
        3431,
        11202,
        11202,
        3431,
        3431,
        11202,
        1454
    ],
    "Sale Date": [
        "14/1/2023",
        "15/1/2023",
        "16/1/2023",
        "17/1/2023",
        "17/1/2023",
        "19/1/2023",
        "20/1/2023",
        None,
        "22/1/2023"
    ]
}

df = pd.DataFrame(data)
# حذف ردیف‌های با داده‌های گمشده و ذخیره تغییرات
df.dropna(inplace=True)

# حذف ردیف‌های با قیمت فروش گمشده
df.dropna(inplace=True, subset=["Sale Price"])

# پر کردن مقادیر گمشده با عدد 999 و چاپ DataFrame
print(df.fillna(999))

# پر کردن مقادیر گمشده در ستون MRP با عدد 22222 و چاپ
print(df["Mrp"].fillna(22222))

# محاسبه میانگین MRP و چاپ آن
print(df["Mrp"].mean())

# پر کردن مقادیر گمشده در ستون MRP با میانگین MRP و چاپ
print(df["Mrp"].fillna(df["Mrp"].mean()))

# محاسبه میانه قیمت فروش و چاپ آن
print(df["Sale Price"].median())

# پر کردن مقادیر گمشده در ستون قیمت فروش با میانه قیمت فروش و چاپ
print(df["Sale Price"].fillna(df["Sale Price"].median()))

# محاسبه مد (mode) برای ستون MRP و پر کردن مقادیر گمشده با آن
x = df["Mrp"].mode()[0]
print(df["Mrp"].fillna(x))

# تبدیل تاریخ فروش به فرمت تاریخ و چاپ آن
df["Sale Date"]= pd.to_datetime(df["Sale Date"])
print(df["Sale Date"])

# تغییر مقدار MRP در ردیف دوم به 69999 و چاپ
df.loc[1, "Mrp"] = 69999
print(df["Mrp"])

# تنظیم حداقل مقدار MRP به 25000 برای ردیف‌های موجود
for i in df.index:
    if df.loc[i, "Mrp"] ==25000:
        df.loc[i, "Mrp"] = 25000
print(df["Mrp"])

# حذف ردیف‌هایی که MRP آن‌ها کمتر از 25000 است
for i in df.index:
    if df.loc[i, "Mrp"]== 25000:
        df.drop(i, inplace=True)
print(df["Mrp"])

# بررسی وجود ردیف‌های تکراری و چاپ نتیجه
print(df.duplicated())

# حذف ردیف‌های تکراری و چاپ DataFrame
print(df.drop_duplicates())

# محاسبه همبستگی بین ستون‌های MRP، قیمت فروش و تاریخ فروش و چاپ
print(df[["Mrp", "Sale Price", "Sale Date"]].corr)

# اضافه کردن یک ستون جدید با مقدار ثابت 5
df["col"] = 5

# حذف ستون‌های MRP و تاریخ فروش از DataFrame
df.drop(["Mrp"], axis=1, inplace=True)
print(df)

# ایجاد یک DataFrame جدید با MRP و تاریخ فروش
x = pd.DataFrame({
    "Mrp": 44444,
    "Sale Date": "1360/04/11"
}, index=[9])

# ادغام DataFrame جدید با DataFrame اصلی
y = pd.concat([x, df])
print(y)

# اضافه کردن یک ردیف جدید به DataFrame با مشخصات تعداد نظرات، MRP و قیمت فروش
df.loc[len(df)+1, ["Number Of Ratings","Mrp", "Sale Price"]] = [55555, 888888, 2]

# حذف ردیف اول از DataFrame
df.drop(0, inplace=True)
print(df)

#   محاسبه میانگین قیمت فروش برای هر محصول و ذخیره در متغیر x
x  = df.groupby("Product Name")["Sale Price"].mean()

# استخراج مدل‌ها از نام محصول
df['Model'] = df['Product Name'].str.extract(r'(iPhone \d+ \w+)')

# محاسبه میانگین قیمت فروش برای هر مدل
average_prices = df.groupby('Model')['Sale Price'].mean().reset_index()

# محاسبه میانگین قیمت فروش و تعداد نظرات برای هر مدل
result = df.groupby('Model').agg(
    Average_Sale_Price=('Sale Price', 'mean'),
    Average_Number_Of_Ratings=('Number Of Ratings', 'mean')
).reset_index()
# نمایش نتایج
print(result)

# شناسایی مدل‌هایی با بیشترین و کمترین میانگین قیمت فروش
max_price_model = average_prices.loc[average_prices['Sale Price'].idxmax()]
min_price_model = average_prices.loc[average_prices['Sale Price'].idxmin()]

print("میانگین قیمت فروش برای هر مدل:")
print(average_prices)
print("\nمدل با بیشترین قیمت فروش:", max_price_model)
print("مدل با کمترین قیمت فروش:", min_price_model)

# اضافه کردن تعداد نظرات به DataFrame
df['Number Of Ratings'] = [3431, 3431, 3431, 11202, 11202, 3431, 3431, 11202, 1454]

# رسم نمودار پراکندگی
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Number Of Ratings', y='Sale Price')
plt.title('تعداد نظرات در برابر قیمت فروش')
plt.xlabel('تعداد نظرات')
plt.ylabel('قیمت فروش')
plt.show()

# محاسبه همبستگی
correlation = df[['Number Of Ratings', 'Sale Price']].corr().iloc[0, 1]
print(f'همبستگی بین تعداد نظرات و قیمت فروش: {correlation:.2f}')

# آماده‌سازی داده‌ها
df['Number Of Ratings'] = [3431, 3431, 3431, 11202, 11202, 3431, 3431, 11202, 1454]
df.dropna(inplace=True)

# ویژگی‌ها و هدف
X = df[['Number Of Ratings']]
y = df['Sale Price']

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# مدل رگرسیون جنگلی
model = RandomForestRegressor()
model.fit(X_train, y_train)

# پیش‌بینی
y_pred = model.predict(X_test)

# ارزیابی مدل
mse = mean_squared_error(y_test, y_pred)
print(f'میانگین مربعات خطا: {mse:.2f}')


# اضافه کردن تاریخ فروش به DataFrame
df['Sale Date'] = [
    "14/1/2023",
    "15/1/2023",
    "16/1/2023",
    "17/1/2023",
    "17/1/2023",
    "19/1/2023",
    "20/1/2023",
    None,
    "22/1/2023"
]
df['Sale Date'] = pd.to_datetime(df['Sale Date'], errors='coerce')

# حذف ردیف‌های با تاریخ گمشده
df.dropna(subset=['Sale Date'], inplace=True)

# محاسبه میانگین قیمت فروش بر اساس تاریخ
daily_average = df.groupby('Sale Date')['Sale Price'].mean().reset_index()

# رسم نمودار
plt.figure(figsize=(10, 6))
plt.plot(daily_average['Sale Date'], daily_average['Sale Price'], marker='o')
plt.title('روند میانگین قیمت فروش بر اساس تاریخ')
plt.xlabel('تاریخ')
plt.ylabel('میانگین قیمت فروش')
plt.xticks(rotation=45)
plt.grid()
plt.show()



# محاسبه میانگین قیمت فروش
mean_sale_price = df['Sale Price'].mean()

# شناسایی محصولات با قیمت غیرمعمول
unusual_price_threshold = 1.5 * mean_sale_price
unusual_products = df[df['Sale Price'] > unusual_price_threshold]

print("محصولات با قیمت غیرمعمول:")
print(unusual_products[['Product Name', 'Sale Price']])

#  یک ستون جدید به نام “h” در موقعیت 1
data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
               {'a': 100, 'b': 200, 'c': 300, 'd': 400},
              {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(data)
df.insert(1, "h", [22, 88,99])

# نمایش تعداد ستون‌ها
# print(f"Number of columns: {df.shape[0]}")
# # نمایش  ستون‌ها
# print(f"show columns: {df.columns.tolist()}")


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})


df['Sum'] = df.apply(lambda row: row['A'] + row['B'], axis=1)
print(df["Sum"])
df["Sum"] = df.apply(lambda x:x["A"] + x["B"], axis=1)

# df = pd.DataFrame({'Name': ['Ali', 'Sara', 'Reza'], 'Score': [85, 60, 45]})
# df['Status'] = df['Score'].apply(lambda x: 'Pass' if x >= 50 else 'Fail')
print(df)
