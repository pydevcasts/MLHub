import os
import pandas as pd
import numpy as np
# # مسیر فولدرهای فایل‌های صوتی و متن
audio_folder = './clips'
tsv_folder = './text'

# بارگذاری فایل‌های صوتی
audio_files = [f for f in os.listdir(audio_folder) if f.endswith('.mp3') or f.endswith('.wav')]

# بارگذاری متن‌ها از تمام فایل‌های TSV
texts = {}
for tsv_file in os.listdir(tsv_folder):
    if tsv_file.endswith('.tsv'):
        tsv_path = os.path.join(tsv_folder, tsv_file)
        df_tsv = pd.read_csv(tsv_path, sep='\t', header=0)  # یا header=None اگر هدر وجود نداشته باشد
        
        # نمایش تعداد ستون‌ها و نام‌های آن‌ها
        # print(f"Processing {tsv_file}:")
        # print(f"Number of columns: {df_tsv.shape[1]}")
        # print(f"Columns: {df_tsv.columns.tolist()}")

        # بررسی نام ستون‌ها و تنظیم آن‌ها بر اساس تعداد واقعی
        if 'path' in df_tsv.columns and 'sentence' in df_tsv.columns:
            for index, row in df_tsv.iterrows():
                audio_file_name = row['path']  # نام فایل صوتی
                sentence_text = row['sentence']  # متن مربوط به فایل صوتی
                
                # ذخیره متن در دیکشنری با نام فایل صوتی به عنوان کلید
                texts[audio_file_name] = sentence_text

# ساخت DataFrame
df = pd.DataFrame(list(texts.items()), columns=['audio_file', 'text'])
# print(df)

# بررسی وجود فایل‌های صوتی
df['audio_exists'] = df['audio_file'].apply(lambda x: os.path.exists(os.path.join(audio_folder, x)))

# نمایش فایل‌هایی که وجود ندارند
missing_audio = df[~df['audio_exists']]
# print("Missing audio files:")
# print(missing_audio[['audio_file']])
# 1. تعداد کل فایل‌های صوتی و متن‌ها
total_audio_files = df['audio_file'].nunique()  # تعداد فایل‌های صوتی منحصر به فرد
total_texts = df['text'].count()  # تعداد متن‌ها
print(f"Total unique audio files: {total_audio_files}")
print(f"Total texts: {total_texts}")



# بررسی وجود ستون‌های up_votes و down_votes
if 'up_votes' in df_tsv.columns and 'down_votes' in df_tsv.columns:
    print("Up votes distribution:")
    print(df_tsv['up_votes'].describe())  # توزیع up_votes

    print("Down votes distribution:")
    print(df_tsv['down_votes'].describe())  # توزیع down_votes

    # توزیع تعداد کل رای‌ها
    df_tsv['total_votes'] = df_tsv['up_votes'] + df_tsv['down_votes']
    print("Total votes distribution:")
    print(df_tsv['total_votes'].describe())



# 3. تجزیه و تحلیل جملات
# اضافه کردن طول جملات و تعداد کلمات به DataFrame
df['sentence_length'] = df['text'].apply(len)  # طول هر جمله
df['word_count'] = df['text'].apply(lambda x: len(x.split()))  # تعداد کلمات در هر جمله

# نمایش آمار توصیفی برای طول جملات و تعداد کلمات
print("Sentence length distribution:")
print(df['sentence_length'].describe())

print("Word count distribution:")
print(df['word_count'].describe())

# نمایش نمونه‌ای از جملات و ویژگی‌های آن‌ها
print("Sample sentences with their lengths and word counts:")
print(df[['text', 'sentence_length', 'word_count']].head())
# ===============================================================
import pandas as pd
import re

import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# فرض کنید که df قبلاً ایجاد شده است و شامل ستون 'text' است

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