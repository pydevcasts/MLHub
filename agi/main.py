
# from analyze import *
import pandas as pd
import re
from analyze import process_data 
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# فرض کنید که df قبلاً ایجاد شده است و شامل ستون 'text' است
df = process_data()
# 1. پاک‌سازی متن‌ها
def clean_text(text):
    # تبدیل به حروف کوچک
    text = text.lower()
    # حذف نشانه‌گذاری
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    # حذف کلمات بی‌معنی (stop words)
    # برای این کار می‌توانید از یک لیست از کلمات بی‌معنی استفاده کنید
    # به عنوان مثال:
    stop_words = set(['و', 'در', 'به', 'از', 'که', 'این', 'برای', 'است', 'با', 'هم', 'اما', 'اگر'])
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

# پاک‌سازی متن‌ها
df['cleaned_text'] = df['text'].apply(clean_text)

# 2. تبدیل داده‌ها به فرمت مناسب
# استفاده از TF-IDF برای تبدیل متن به ویژگی‌های عددی
tfidf_vectorizer = TfidfVectorizer(max_features=5000)  # می‌توانید تعداد ویژگی‌ها را تنظیم کنید
X = tfidf_vectorizer.fit_transform(df['cleaned_text']).toarray()  # ویژگی‌های عددی
y = df['audio_file']  # یا هر برچسب دیگری که دارید

# تقسیم داده‌ها به مجموعه‌های آموزشی و آزمایشی
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# نمایش ابعاد داده‌ها
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")

