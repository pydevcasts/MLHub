
### 1. نصب PyQt6

اولین قدم نصب PyQt6 است. از آنجا که PyQt6 به صورت یک بسته پایتون است، می‌توانید آن را با pip نصب کنید. در ترمینال یا CMD دستور زیر را اجرا کنید:

```bash
pip install PyQt6
```

### 2. ساختار یک برنامه PyQt6

یک برنامه PyQt6 معمولاً شامل مراحل زیر است:

- **ایجاد یک شیء QApplication**
- **ایجاد ویجت‌ها و تنظیمات آن‌ها**
- **نمایش پنجره**
- **مدیریت رویدادها**

در اینجا یک مثال ساده از یک برنامه PyQt6 را بررسی می‌کنیم:

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # تنظیم عنوان و اندازه پنجره
        self.setWindowTitle("Hello PyQt6")
        self.setGeometry(100, 100, 600, 400)

        # اضافه کردن یک برچسب
        label = QLabel("سلام به PyQt6!", self)
        label.setGeometry(200, 150, 200, 50)

# اجرای برنامه
app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

### 3. توضیحات کد

- **import sys**: برای مدیریت سیستم و ورودی/خروجی استفاده می‌شود.
- **QApplication**: این کلاس برای مدیریت برنامه PyQt6 و رویدادها استفاده می‌شود.
- **QMainWindow**: این کلاس برای ایجاد پنجره‌های اصلی استفاده می‌شود.
- **QLabel**: برای نمایش متن یا تصویر استفاده می‌شود.

### 4. کار با Layoutها

برای چیدمان ویجت‌ها در پنجره، می‌توانید از Layoutها استفاده کنید. در اینجا یک مثال از استفاده از `QVBoxLayout` برای چیدمان عمودی ویجت‌ها آورده شده است:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Layout Example")
        self.setGeometry(100, 100, 400, 300)

        # ایجاد یک ویجت مرکزی
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # ایجاد و تنظیم Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # اضافه کردن ویجت‌ها به Layout
        label1 = QLabel("برچسب 1", self)
        label2 = QLabel("برچسب 2", self)
        layout.addWidget(label1)
        layout.addWidget(label2)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

### 5. سیگنال‌ها و اسلات‌ها

در PyQt6، می‌توانید از سیگنال‌ها و اسلات‌ها برای مدیریت رویدادها استفاده کنید. در اینجا یک مثال از دکمه و نحوه واکنش به کلیک آن آورده شده است:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Signal and Slot Example")
        self.setGeometry(100, 100, 300, 200)

        # ایجاد دکمه
        button = QPushButton("کلیک کن!", self)
        button.setGeometry(100, 70, 100, 30)

        # اتصال سیگنال به اسلات
        button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        QMessageBox.information(self, "پیغام", "دکمه کلیک شد!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

### 6. ایجاد منوها

برای ایجاد منوها در برنامه خود، می‌توانید از `QMenuBar` استفاده کنید:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu Example")
        self.setGeometry(100, 100, 400, 300)

        # ایجاد منو
        menubar = self.menuBar()
        file_menu = menubar.addMenu("فایل")

        # ایجاد اکشن و اتصال به سیگنال
        exit_action = QAction("خروج", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

### 7. استفاده از دیالوگ‌ها

شما می‌توانید از دیالوگ‌ها برای دریافت ورودی از کاربر استفاده کنید:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Dialog Example")
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("ورود نام", self)
        button.setGeometry(100, 70, 100, 30)
        button.clicked.connect(self.show_input_dialog)

    def show_input_dialog(self):
        text, ok = QInputDialog.getText(self, "ورود نام", "نام خود را وارد کنید:")
        if ok:
            QMessageBox.information(self, "پیغام", f"سلام، {text}!")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

### 8. استفاده از تصاویر

برای نمایش تصاویر می‌توانید از `QLabel` و متد `setPixmap` استفاده کنید:

```python
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Example")
        self.setGeometry(100, 100, 400, 300)

        label = QLabel(self)
        pixmap = QPixmap("path_to_your_image.png")  # مسیر تصویر
        label.setPixmap(pixmap)
        label.setGeometry(10, 10, pixmap.width(), pixmap.height())

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())
```

### 9. بسته‌بندی برنامه

برای بسته‌بندی برنامه به یک فایل اجرایی (Executable)، می‌توانید از ابزارهایی مانند `PyInstaller` استفاده کنید. برای نصب PyInstaller:

```bash
pip install pyinstaller
```

سپس می‌توانید برنامه خود را بسته‌بندی کنید:

```bash
pyinstaller --onefile your_script.py
```

این دستور یک فایل اجرایی مستقل ایجاد می‌کند که می‌توانید آن را به دیگران ارسال کنید.
---
برای ایجاد تب (Tab) در PyQt6، شما می‌توانید از کلاس `QTabWidget` استفاده کنید. این کلاس به شما این امکان را می‌دهد که چندین تب ایجاد کنید و محتوای مختلفی را در هر تب نمایش دهید. در زیر یک مثال ساده برای ایجاد یک پنجره با تب‌ها آورده شده است:

```python
import sys
from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # ایجاد یک QTabWidget
        self.tab_widget = QTabWidget()

        # ایجاد تب‌ها
        self.create_tabs()

        # تنظیم لایه اصلی
        layout = QVBoxLayout()
        layout.addWidget(self.tab_widget)
        self.setLayout(layout)

        self.setWindowTitle("Tab Example")
        self.setGeometry(100, 100, 400, 300)

    def create_tabs(self):
        # ایجاد تب اول
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QLabel("This is Tab 1"))
        tab1.setLayout(tab1_layout)

        # ایجاد تب دوم
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QLabel("This is Tab 2"))
        tab2.setLayout(tab2_layout)

        # اضافه کردن تب‌ها به QTabWidget
        self.tab_widget.addTab(tab1, "Tab 1")
        self.tab_widget.addTab(tab2, "Tab 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
```

### توضیحات کد:
- ابتدا `QApplication` و `QTabWidget` از ماژول `PyQt6.QtWidgets` ایمپورت می‌شوند.
- یک کلاس `MyWindow` تعریف می‌شود که از `QWidget` ارث بری می‌کند.
- در متد `__init__`، یک `QTabWidget` ایجاد و تب‌ها را با متد `create_tabs` ایجاد و اضافه می‌کنیم.
- در هر تب، یک `QWidget` جدید ایجاد می‌شود و به آن یک لایه عمودی (`QVBoxLayout`) اضافه می‌شود که حاوی یک برچسب (`QLabel`) است.
- در انتها، پنجره ایجاد شده نمایش داده می‌شود.

شما می‌توانید تب‌های بیشتری اضافه کنید و محتوای مختلفی را در هر تب قرار دهید.
---
### 10. منابع یادگیری بیشتر

- **مستندات رسمی PyQt6**: [مستندات PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)
- **کتاب‌های آموزشی**: کتاب‌هایی در مورد PyQt6 وجود دارد که می‌تواند به شما کمک کند.
- **ویدئوهای آموزشی**: YouTube و سایر پلتفرم‌ها ویدئوهای آموزشی زیادی درباره PyQt6 دارند.
---
