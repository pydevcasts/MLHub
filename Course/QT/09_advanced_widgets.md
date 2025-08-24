## صفحه ۹ – ویجت‌های پیشرفته در PyQt6

### ۱. تقویم (QCalendarWidget) 📅

این ویجت یک تقویم کامل نمایش می‌دهد و کاربر می‌تواند یک تاریخ انتخاب کند.

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Calendar Example")
window.resize(400, 300)

layout = QVBoxLayout()

calendar = QCalendarWidget()
label = QLabel("Select a date")

# Update label when date is changed
calendar.selectionChanged.connect(lambda: label.setText(calendar.selectedDate().toString()))

layout.addWidget(calendar)
layout.addWidget(label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
```

📌 نتیجه: کاربر می‌تواند تاریخ را از تقویم انتخاب کند و همان تاریخ در برچسب نمایش داده می‌شود.

---

### ۲. اسلایدر (QSlider) 🎚️

اسلایدر برای گرفتن عددی بین یک بازه استفاده می‌شود (مثلاً تنظیم صدا یا روشنایی).

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QLabel
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Slider Example")
window.resize(300, 200)

layout = QVBoxLayout()

slider = QSlider(Qt.Orientation.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(50)

label = QLabel("Value: 50")

# Update label when slider moves
slider.valueChanged.connect(lambda value: label.setText(f"Value: {value}"))

layout.addWidget(slider)
layout.addWidget(label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
```

📌 نتیجه: یک اسلایدر افقی نمایش داده می‌شود که مقدارش بین ۰ تا ۱۰۰ تغییر می‌کند و مقدار فعلی در برچسب نشان داده می‌شود.

---

### ۳. Progress Bar 🔄

این ویجت برای نمایش وضعیت پیشرفت یک عملیات (مثل دانلود یا نصب) استفاده می‌شود.

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton
from PyQt6.QtCore import QTimer

class ProgressExample(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Bar Example")
        self.resize(300, 150)

        self.layout = QVBoxLayout()

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.button = QPushButton("Start")

        self.layout.addWidget(self.progress)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Timer to update progress
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        self.button.clicked.connect(self.start_progress)
        self.value = 0

    def start_progress(self):
        self.value = 0
        self.progress.setValue(0)
        self.timer.start(100)

    def update_progress(self):
        self.value += 5
        self.progress.setValue(self.value)
        if self.value >= 100:
            self.timer.stop()

app = QApplication(sys.argv)
window = ProgressExample()
window.show()
sys.exit(app.exec())
```

📌 نتیجه: با کلیک روی دکمه، نوار پیشرفت شروع به پر شدن می‌کند تا به ۱۰۰ برسد.

---

✅ حالا شما با چند ویجت پیشرفته‌ی کاربردی آشنا شدید که تقریباً در همه‌ی نرم‌افزارهای جدی استفاده می‌شوند.

---

در **صفحه ۱۰** یاد می‌گیریم چطور با استفاده از **StyleSheet** ظاهر برنامه‌هایمان را زیباتر کنیم؛ مثل تغییر رنگ‌ها، فونت‌ها و طراحی ظاهری مدرن. 🎨✨

