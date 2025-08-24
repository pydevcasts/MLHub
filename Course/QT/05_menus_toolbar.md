## صفحه ۵ – منوها و نوار ابزار در PyQt6

بیشتر نرم‌افزارهایی که استفاده می‌کنیم (مثل ورد، مرورگر یا حتی نوت‌پد) دارای **منو** هستند؛ جایی که گزینه‌هایی مثل *File → Open → Save* یا *Help → About* قرار دارند. در PyQt6 ساخت منوها بسیار ساده است و با چند خط کد انجام می‌شود.

---

### ساختار اصلی منو

برای استفاده از منو و نوار ابزار باید به‌جای QWidget از **QMainWindow** استفاده کنیم، چون این کلاس امکاناتی مثل منوبار و استاتوس‌بار را به ما می‌دهد.

---

### مثال: ساخت یک منوی ساده

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Menu Example")
        self.resize(500, 400)

        # Create a text editor as central widget
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Create menu bar
        menu_bar = self.menuBar()

        # Create File menu
        file_menu = menu_bar.addMenu("File")

        # Create actions
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)

        # Add actions to File menu
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()  # Add a separator line
        file_menu.addAction(exit_action)

        # Connect exit action
        exit_action.triggered.connect(self.close)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
```

---

### توضیح کد

* به‌جای QWidget از QMainWindow استفاده کردیم.
* با `menuBar()` یک نوار منو ساختیم.
* با `addMenu("File")` منوی File را ایجاد کردیم.
* هر گزینه داخل منو یک **Action** است که با QAction ساخته می‌شود.
* با `addSeparator()` خط جداکننده ایجاد کردیم.
* در نهایت، گزینه‌ی Exit را به تابع `close` وصل کردیم تا با انتخاب آن، برنامه بسته شود.

---

### افزودن نوار ابزار (ToolBar)

می‌توانیم همان Actionها را در یک **نوار ابزار** هم قرار دهیم:

```python
# Create a toolbar and add actions
tool_bar = self.addToolBar("Main Toolbar")
tool_bar.addAction(new_action)
tool_bar.addAction(open_action)
tool_bar.addAction(save_action)
```

با این کار، یک نوار ابزار زیر منو ظاهر می‌شود و گزینه‌ها به‌صورت دکمه نمایش داده خواهند شد. 🛠️

---

📌 نتیجه:
برنامه‌ی شما حالا منوی File دارد که شامل گزینه‌های New، Open، Save و Exit است. همچنین می‌توانید با اضافه کردن ToolBar نرم‌افزارتان را حرفه‌ای‌تر کنید. ✨

---

✅ در **صفحه ۶** می‌خواهیم سراغ یکی از پرکاربردترین بخش‌ها برویم: **باز کردن و ذخیره‌سازی فایل با QFileDialog**. 📂

---
