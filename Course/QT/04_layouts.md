## صفحه ۴ – مدیریت چیدمان‌ها در PyQt6

### چرا Layout مهم است؟

* باعث می‌شود ویجت‌ها به‌طور خودکار مرتب شوند.
* اگر کاربر اندازه‌ی پنجره را تغییر دهد، ویجت‌ها به‌طور مناسب جا‌به‌جا یا تغییر اندازه می‌دهند.
* ظاهر نرم‌افزار حرفه‌ای‌تر می‌شود.

---

### انواع Layoutهای پرکاربرد

* **QVBoxLayout** ➡️ چیدمان عمودی (از بالا به پایین)
* **QHBoxLayout** ➡️ چیدمان افقی (از چپ به راست)
* **QGridLayout** ➡️ چیدمان جدولی (ردیف و ستون)

---

### مثال: فرم ورود با Layout

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

app = QApplication(sys.argv)

# Create main window
window = QWidget()
window.setWindowTitle("Login Form with Layout")
window.resize(300, 200)

# Create widgets
label_user = QLabel("Username:")
input_user = QLineEdit()

label_pass = QLabel("Password:")
input_pass = QLineEdit()
input_pass.setEchoMode(QLineEdit.EchoMode.Password)  # Hide password

login_button = QPushButton("Login")

# Create vertical layout
layout = QVBoxLayout()
layout.addWidget(label_user)
layout.addWidget(input_user)
layout.addWidget(label_pass)
layout.addWidget(input_pass)
layout.addWidget(login_button)

# Set layout for window
window.setLayout(layout)

# Show the window
window.show()

sys.exit(app.exec())
```

---

### توضیح کد

* در این مثال به جای استفاده از `move`، همه‌ی ویجت‌ها را به یک **چیدمان عمودی** (QVBoxLayout) اضافه کردیم.
* متد `addWidget` ویجت‌ها را به ترتیب به Layout اضافه می‌کند.
* با `setLayout` کل چیدمان به پنجره داده می‌شود.
* برای ورودی رمز عبور از ویژگی `setEchoMode` استفاده کردیم تا کاراکترهای واردشده به‌صورت نقطه نمایش داده شوند. 🔒

---

📌 نتیجه:
شما یک **فرم ورود ساده** دارید که کاملاً مرتب و واکنش‌پذیر است. اگر پنجره را کوچک و بزرگ کنید، ویجت‌ها همچنان منظم باقی می‌مانند. ✨

---

✅ حالا که با چیدمان‌ها آشنا شدید، در **صفحه ۵** یاد می‌گیریم چطور یک **منو و نوار ابزار** بسازیم تا برنامه حرفه‌ای‌تر شود. 🛠️

