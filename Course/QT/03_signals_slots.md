## صفحه ۳ – سیگنال‌ها و اسلات‌ها در PyQt6

تا الان فقط ویجت‌های ثابت ساختیم. اما یک برنامه‌ی واقعی باید **واکنش‌پذیر** باشد؛ یعنی وقتی کاربر روی دکمه کلیک کرد یا متنی نوشت، تغییری در برنامه رخ بدهد. در PyQt6 این کار با **Signal** و **Slot** انجام می‌شود.

### مفهوم سیگنال و اسلات

* **سیگنال (Signal):** یک رویداد است که توسط ویجت ارسال می‌شود. مثلاً وقتی روی دکمه کلیک می‌کنیم، سیگنال "کلیک شد" فرستاده می‌شود.
* **اسلات (Slot):** یک تابع یا متد است که به سیگنال وصل می‌شود و وقتی سیگنال رخ داد، اجرا می‌شود.

---

### مثال: تغییر متن برچسب با کلیک روی دکمه

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)

# Create main window
window = QWidget()
window.setWindowTitle("Signal and Slot Example")
window.resize(400, 300)

# Create a label
label = QLabel("Waiting for action...", window)
label.move(50, 50)

# Create a text input
text_input = QLineEdit(window)
text_input.move(50, 100)
text_input.resize(200, 30)

# Create a button
button = QPushButton("Change Label", window)
button.move(50, 150)

# Define slot function
def change_label_text():
    user_text = text_input.text()  # Get text from input
    label.setText(user_text)       # Set label text

# Connect signal (button click) to slot (function)
button.clicked.connect(change_label_text)

# Show the window
window.show()

sys.exit(app.exec())
```

---

### توضیح کد:

* وقتی کاربر روی دکمه کلیک می‌کند، سیگنال `clicked` ارسال می‌شود.
* ما با `.connect` این سیگنال را به تابع `change_label_text` وصل کردیم.
* تابع ما متن وارد شده در `QLineEdit` را می‌گیرد و در `QLabel` نمایش می‌دهد.

📌 حالا برنامه‌ی شما تعامل‌پذیر شده است! کاربر متنی در ورودی می‌نویسد، روی دکمه کلیک می‌کند و متن برچسب تغییر می‌کند. ✨

---

✅ تا اینجا توانستیم ویجت‌ها را به هم متصل کنیم.
در **صفحه ۴** می‌رویم سراغ چیزی بسیار کاربردی‌تر: **مدیریت چیدمان‌ها (Layouts)** برای اینکه برنامه مرتب و حرفه‌ای دیده شود. 🖼️

