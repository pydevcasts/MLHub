# import os
# import librosa
# import numpy as np
# import pandas as pd

# audio_folder = './clips'
# low_quality_files = []

# def check_audio_quality(file_path):
#     try:
#         audio, sr = librosa.load(file_path, sr=None)
        
#         # محاسبه RMS
#         rms = np.sqrt(np.mean(audio**2))
        
#         # محاسبه سطح نویز (SNR)
#         noise_level = np.mean(np.abs(audio))
#         snr = 20 * np.log10(rms / noise_level) if noise_level > 0 else -np.inf
        
#         # معیارهای کیفیت
#         if rms < 0.01 or snr < 10:  # این مقادیر می‌توانند بر اساس نیاز شما تغییر کنند
#             return True  # کیفیت پایین
#         else:
#             return False  # کیفیت خوب
#     except Exception as e:
#         print(f"Error processing {file_path}: {e}")
#         return False

# # بررسی همه فایل‌های صوتی در پوشه
# for audio_file in os.listdir(audio_folder):
#     if audio_file.endswith('.wav') or audio_file.endswith('.mp3'):
#         file_path = os.path.join(audio_folder, audio_file)
#         if check_audio_quality(file_path):
#             low_quality_files.append(audio_file)

# # نمایش فایل‌های با کیفیت پایین
# print(f"Files with low quality:{len(low_quality_files)}")
# # for file in low_quality_files:
# #     print(file)


import os
import librosa
import numpy as np
import pandas as pd

audio_folder = './wav'
low_quality_files = []

def calculate_snr(audio):
    """محاسبه نسبت سیگنال به نویز (SNR)"""
    signal_power = np.mean(audio**2)
    noise_power = np.var(audio)
    if noise_power == 0:
        return np.inf  # اگر نویز وجود نداشته باشد
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

def calculate_thd(audio, sr, n_harmonics=5):
    """محاسبه اعوجاج هارمونیک کل (THD)"""
    fft = np.fft.fft(audio)
    magnitude = np.abs(fft)
    fundamental = np.max(magnitude)
    harmonic_indices = np.arange(2, n_harmonics + 2)
    harmonic_magnitudes = magnitude[harmonic_indices]
    thd = np.sqrt(np.sum(harmonic_magnitudes**2)) / fundamental
    return thd

def calculate_spectral_flatness(audio):
    """محاسبه Spectral Flatness"""
    spectrum = np.abs(np.fft.fft(audio))
    geometric_mean = np.exp(np.mean(np.log(spectrum + 1e-10)))
    arithmetic_mean = np.mean(spectrum)
    flatness = geometric_mean / arithmetic_mean
    return flatness

def check_audio_quality(file_path):
    try:
        audio, sr = librosa.load(file_path, sr=None)
        
        # محاسبه SNR
        snr = calculate_snr(audio)
        
        # محاسبه THD
        thd = calculate_thd(audio, sr)
        
        # محاسبه Spectral Flatness
        flatness = calculate_spectral_flatness(audio)
        
        # معیارهای کیفیت
        if snr < 20 or thd > 0.1 or flatness < 0.1:  # مقادیر قابل تنظیم
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
print(f"Files with low quality: {len(low_quality_files)}")
# for file in low_quality_files:
#     print(file)