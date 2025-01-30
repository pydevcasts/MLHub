import os
import numpy as np
import pandas as pd
import librosa
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical

# 1. بارگذاری داده‌ها
audio_folder = './clips'
tsv_folder = './text'
texts = {}

# پردازش فایل‌های TSV
for tsv_file in os.listdir(tsv_folder):
    if tsv_file.endswith('.tsv'):
        tsv_path = os.path.join(tsv_folder, tsv_file)
        df_tsv = pd.read_csv(tsv_path, sep='\t', header=0)

        if {'path', 'sentence'}.issubset(df_tsv.columns):
            for index, row in df_tsv.iterrows():
                audio_file_name = row['path']
                sentence_text = row['sentence']
                texts[audio_file_name] = sentence_text

# ایجاد DataFrame
df = pd.DataFrame(list(texts.items()), columns=['audio_file', 'text'])

# 2. ایجاد Spectrogram
def create_spectrogram(file_name):
    audio, sr = librosa.load(file_name, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=audio, sr=sr)
    spectrogram_db = librosa.power_to_db(spectrogram, ref=np.max)
    return spectrogram_db

# ایجاد Spectrogram برای هر فایل صوتی
df['spectrogram'] = df['audio_file'].apply(lambda x: create_spectrogram(os.path.join(audio_folder, x)))

# 3. آماده‌سازی داده‌ها برای CNN
X = np.array(list(df['spectrogram']))
y = df['text']
le = LabelEncoder()
y_encoded = le.fit_transform(y)
y_categorical = to_categorical(y_encoded)

# تقسیم داده‌ها
X_train, X_test, y_train, y_test = train_test_split(X, y_categorical, test_size=0.2, random_state=42)

# 4. ساخت مدل CNN
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(X_train.shape[1], X_train.shape[2], 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten()) 
model.add(Dense(64, activation='relu'))
model.add(Dense(len(le.classes_), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5. آموزش مدل
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# 6. ارزیابی مدل
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {accuracy} and Loss: {loss}")