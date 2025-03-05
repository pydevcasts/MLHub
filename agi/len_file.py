import os

# مسیر پوشه
folder_path = './wav'  # مسیر پوشه خود را مشخص کنید

# شمارش فایل‌ها
file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

print(f"Number of files in '{folder_path}': {file_count}")