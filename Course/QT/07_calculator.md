## صفحه ۷ – پروژه ماشین حساب ساده

ماشین حساب ما شامل دکمه‌های اعداد، چهار عمل اصلی و یک نمایشگر خواهد بود.

---

### کد پروژه

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Simple Calculator")
        self.resize(300, 400)

        # Create display
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignmentFlag.Right)  # Align text to right
        self.display.setReadOnly(True)  # User cannot type directly

        # Create grid layout
        grid = QGridLayout()
        grid.addWidget(self.display, 0, 0, 1, 4)  # Span display across 4 columns

        # Buttons for calculator
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Add buttons to grid
        for text, row, col in buttons:
            button = QPushButton(text)
            button.clicked.connect(self.on_button_clicked)
            grid.addWidget(button, row, col)

        self.setLayout(grid)

    def on_button_clicked(self):
        # Get text of clicked button
        button = self.sender()
        text = button.text()

        if text == "=":
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

app = QApplication(sys.argv)
window = Calculator()
window.show()
sys.exit(app.exec())
```

---

### توضیح کد

* از **QGridLayout** استفاده کردیم تا دکمه‌ها مانند صفحه‌کلید ماشین حساب مرتب شوند.
* نمایشگر برنامه با **QLineEdit** ساخته شده که فقط خروجی نشان می‌دهد.
* وقتی روی دکمه‌ای کلیک می‌کنیم، متن آن به محتوای نمایشگر اضافه می‌شود.
* وقتی روی دکمه "=" می‌زنیم، رشته‌ی موجود با دستور `eval` محاسبه و نتیجه نمایش داده می‌شود.
* اگر خطایی رخ دهد (مثلاً کاربر تقسیم بر صفر بزند)، خروجی "Error" نمایش داده می‌شود.

---

📌 نتیجه:
برنامه‌ی شما حالا یک ماشین حساب ساده دارد که چهار عمل اصلی (+, -, \*, /) را انجام می‌دهد. 🧮

---

✅ در **صفحه ۸** یک پروژه‌ی دیگر خواهیم ساخت: **دفترچه یادداشت ساده (Text Editor)** با قابلیت نوشتن متن، ذخیره‌سازی و باز کردن فایل. 📝

