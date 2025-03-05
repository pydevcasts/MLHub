import os
import torchaudio
import torch
import numpy as np

# مسیر پوشه حاوی فایل‌های صوتی
audio_folder = './clips'  # مسیر پوشه خود را مشخص کنید
output_folder = './final_audio'  # مسیر ذخیره فایل‌های بهبود یافته

# ایجاد پوشه خروجی در صورت عدم وجود
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# پردازش فایل‌های صوتی
for audio_file in os.listdir(audio_folder):
    if audio_file.endswith('.mp3') or audio_file.endswith('.wav'):
        file_path = os.path.join(audio_folder, audio_file)
        
        try:
            # بارگذاری فایل صوتی با torchaudio
            audio, sr = torchaudio.load(file_path)

            # بررسی طول سیگنال
            if audio.shape[1] < sr:  # کمتر از 1 ثانیه
                print(f"Audio file {audio_file} is too short for noise reduction. Skipping.")
                continue
            
            # بررسی وجود سیگنال‌های NaN یا inf
            if torch.any(torch.isnan(audio)) or torch.any(torch.isinf(audio)):
                print(f"Audio file {audio_file} contains NaN or infinite values. Skipping.")
                continue
            
            # کاهش نویز با استفاده از فیلتر پایین‌گذر (Low-pass Filter)
            try:
                # اعمال فیلتر پایین‌گذر
                cutoff_freq = 3000  # فرکانس قطع (بر حسب هرتز)
                filtered_audio = torchaudio.functional.lowpass_biquad(audio, sr, cutoff_freq=cutoff_freq)

                # اعمال فیلتر بالا‌گذر (High-pass Filter) برای حذف نویز فرکانس پایین
                cutoff_freq_high = 200  # فرکانس قطع (بر حسب هرتز)
                filtered_audio = torchaudio.functional.highpass_biquad(filtered_audio, sr, cutoff_freq=cutoff_freq_high)

            except Exception as filter_error:
                print(f"Noise reduction failed for {audio_file}: {filter_error}. Skipping this file.")
                continue  # ادامه به فایل بعدی
            
            # ذخیره فایل بهبود یافته
            output_file_path = os.path.join(output_folder, audio_file)
            torchaudio.save(output_file_path, filtered_audio, sr)

            print(f"Processed {audio_file} and saved to {output_file_path}")
        
        except Exception as e:
            print(f"Error processing {audio_file}: {e}. Skipping this file.")
            continue  # ادامه به فایل بعدی

print("All files processed.")
# ==============================================

# import os
# import numpy as np
# from scipy.signal import butter, filtfilt
# from pydub import AudioSegment
# from pydub.playback import play

# # مسیر پوشه حاوی فایل‌های صوتی
# audio_folder = './clips'  # مسیر پوشه خود را مشخص کنید
# output_folder = './enhanced_audio'  # مسیر ذخیره فایل‌های بهبود یافته

# # ایجاد پوشه خروجی در صورت عدم وجود
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # طراحی فیلتر پایین‌گذر باترورث
# def butter_lowpass(cutoff, sr, order=5):
#     nyquist = 0.5 * sr
#     normal_cutoff = cutoff / nyquist
#     b, a = butter(order, normal_cutoff, btype='low', analog=False)
#     return b, a

# # اعمال فیلتر پایین‌گذر
# def lowpass_filter(data, cutoff, sr, order=5):
#     b, a = butter_lowpass(cutoff, sr, order=order)
#     y = filtfilt(b, a, data)
#     return y

# # پردازش فایل‌های صوتی
# for audio_file in os.listdir(audio_folder):
#     if audio_file.endswith('.mp3') or audio_file.endswith('.wav'):
#         file_path = os.path.join(audio_folder, audio_file)
        
#         try:
#             # بارگذاری فایل صوتی با pydub
#             audio = AudioSegment.from_file(file_path)

#             # تبدیل به آرایه numpy
#             samples = np.array(audio.get_array_of_samples())
#             sr = audio.frame_rate

#             # بررسی طول سیگنال
#             if len(samples) < sr:  # کمتر از 1 ثانیه
#                 print(f"Audio file {audio_file} is too short for noise reduction. Skipping.")
#                 continue
            
#             # بررسی وجود سیگنال‌های NaN یا inf
#             if np.any(np.isnan(samples)) or np.any(np.isinf(samples)):
#                 print(f"Audio file {audio_file} contains NaN or infinite values. Skipping.")
#                 continue
            
#             # کاهش نویز با فیلتر پایین‌گذر
#             try:
#                 cutoff_freq = 3000  # فرکانس قطع (بر حسب هرتز)
#                 filtered_samples = lowpass_filter(samples, cutoff_freq, sr)

#                 # تبدیل به AudioSegment
#                 filtered_audio = AudioSegment(
#                     filtered_samples.tobytes(),
#                     frame_rate=sr,
#                     sample_width=audio.sample_width,
#                     channels=audio.channels
#                 )

#             except Exception as filter_error:
#                 print(f"Noise reduction failed for {audio_file}: {filter_error}. Skipping this file.")
#                 continue  # ادامه به فایل بعدی
            
#             # ذخیره فایل بهبود یافته
#             output_file_path = os.path.join(output_folder, audio_file)
#             filtered_audio.export(output_file_path, format="wav")

#             print(f"Processed {audio_file} and saved to {output_file_path}")
        
#         except Exception as e:
#             print(f"Error processing {audio_file}: {e}. Skipping this file.")
#             continue  # ادامه به فایل بعدی

# print("All files processed.")