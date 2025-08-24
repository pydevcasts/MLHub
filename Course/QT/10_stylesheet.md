## صفحه ۱۰ – زیباسازی رابط کاربری با StyleSheet

در PyQt6 شما می‌تونید از **StyleSheet** استفاده کنید. این سیستم تقریباً مثل CSS در طراحی وب عمل می‌کنه و می‌شه باهاش رنگ‌ها، فونت‌ها، اندازه‌ها و ظاهر ویجت‌ها رو تغییر داد.

---

### مثال ۱: تغییر رنگ دکمه‌ها

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Styled Buttons")
window.resize(300, 200)

layout = QVBoxLayout()

button1 = QPushButton("Green Button")
button2 = QPushButton("Red Button")

# Apply styles
button1.setStyleSheet("background-color: green; color: white; font-size: 16px; padding: 8px;")
button2.setStyleSheet("background-color: red; color: white; font-weight: bold;")

layout.addWidget(button1)
layout.addWidget(button2)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
```

📌 نتیجه: یک دکمه سبز و یک دکمه قرمز خواهید داشت، با فونت و استایل متفاوت.

---

### مثال ۲: تغییر استایل ویجت‌ها

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Styled Widgets")
window.resize(300, 200)

layout = QVBoxLayout()

label = QLabel("Username:")
textbox = QLineEdit()

# Apply styles
label.setStyleSheet("font-size: 14px; color: navy;")
textbox.setStyleSheet("""
    border: 2px solid gray;
    border-radius: 5px;
    padding: 5px;
    font-size: 14px;
""")

layout.addWidget(label)
layout.addWidget(textbox)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
```

📌 نتیجه: لیبل با رنگ آبی و فونت زیباتر نمایش داده می‌شه و جعبه‌ی متنی هم دارای حاشیه گرد و استایل حرفه‌ای خواهد بود.

---

### نکته‌های مهم در استفاده از StyleSheet

✅ می‌تونید برای هر ویجت جداگانه استایل تعریف کنید.
✅ می‌تونید کلاس یا نام مشخص برای ویجت بذارید و مثل CSS برای همه یکجا استایل اعمال کنید.
✅ می‌تونید انیمیشن و جلوه‌های گرافیکی ساده بسازید.

---

✨ حالا دیگه نه تنها می‌تونید برنامه‌های کاربردی با PyQt6 بسازید، بلکه می‌تونید ظاهرشون رو هم شیک و حرفه‌ای طراحی کنید.

---

📕🎉 به همین ترتیب کتاب ما به پایان رسید:

* از آشنایی با PyQt6 شروع کردیم.
* ویجت‌های ساده مثل دکمه‌ها و لیبل‌ها رو شناختیم.
* پروژه‌های واقعی مثل ماشین حساب 🧮 و دفترچه یادداشت 📝 ساختیم.
* ویجت‌های پیشرفته مثل تقویم 📅، اسلایدر 🎚️ و ProgressBar 🔄 رو یاد گرفتیم.
* و در نهایت با StyleSheet یاد گرفتیم ظاهر برنامه‌هامون رو زیباتر کنیم. 🎨

