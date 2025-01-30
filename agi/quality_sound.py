import os
import librosa
import numpy as np
import pandas as pd

audio_folder = './clips'
low_quality_files = []

def check_audio_quality(file_path):
    try:
        audio, sr = librosa.load(file_path, sr=None)
        
        # محاسبه RMS
        rms = np.sqrt(np.mean(audio**2))
        
        # محاسبه سطح نویز (SNR)
        noise_level = np.mean(np.abs(audio))
        snr = 20 * np.log10(rms / noise_level) if noise_level > 0 else -np.inf
        
        # معیارهای کیفیت
        if rms < 0.01 or snr < 10:  # این مقادیر می‌توانند بر اساس نیاز شما تغییر کنند
            return True  # کیفیت پایین
        else:
            return False  # کیفیت خوب
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# بررسی همه فایل‌های صوتی در پوشه
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith('.wav') or audio_file.endswith('.mp3'):
        file_path = os.path.join(audio_folder, audio_file)
        if check_audio_quality(file_path):
            low_quality_files.append(audio_file)

# نمایش فایل‌های با کیفیت پایین
print(f"Files with low quality:{len(low_quality_files)}")
# for file in low_quality_files:
#     print(file)