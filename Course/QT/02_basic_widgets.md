## صفحه ۲ – ویجت‌های پایه در PyQt6

تا اینجا یک پنجره‌ی خالی ساختیم. اما یک پنجره‌ی خالی به درد ما نمی‌خورد! 😅 حالا وقت آن است که عناصر اصلی یا همان **ویجت‌ها** را به پنجره اضافه کنیم.

### مهم‌ترین ویجت‌های پایه:

* دکمه (QPushButton) ➡️ برای انجام عملیات
* برچسب (QLabel) ➡️ برای نمایش متن
* ورودی متن (QLineEdit) ➡️ برای گرفتن داده از کاربر

### مثال: اضافه کردن چند ویجت ساده

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)

# Create main window
window = QWidget()
window.setWindowTitle("Basic Widgets Example")
window.resize(400, 300)

# Create a label
label = QLabel("Hello PyQt6!", window)
label.move(50, 50)  # Set position

# Create a button
button = QPushButton("Click Me", window)
button.move(50, 100)

# Create a text input
text_input = QLineEdit(window)
text_input.move(50, 150)
text_input.resize(200, 30)  # Set width and height

# Show the window
window.show()

sys.exit(app.exec())
```

### توضیحات:

* `QLabel` یک برچسب ساده برای نمایش متن است.
* `QPushButton` یک دکمه ایجاد می‌کند.
* `QLineEdit` یک جعبه‌ی متنی است که کاربر می‌تواند چیزی در آن تایپ کند.
* متد `move(x, y)` مکان ویجت را روی پنجره مشخص می‌کند.
* متد `resize(w, h)` اندازه‌ی ویجت را تغییر می‌دهد.

💡 با اجرای این برنامه، شما یک برچسب، یک دکمه و یک ورودی متن خواهید داشت.

---

✅ حالا با ویجت‌های پایه آشنا شدید. در صفحه‌ی بعد، یاد می‌گیریم چطور این ویجت‌ها را به هم متصل کنیم تا با کلیک روی دکمه، متن برچسب تغییر کند. این همان **مفهوم سیگنال و اسلات** در PyQt6 است. 🔄

