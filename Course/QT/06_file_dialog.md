## صفحه ۶ – باز کردن و ذخیره‌سازی فایل در PyQt6

یکی از قابلیت‌های اساسی نرم‌افزارها این است که بتوانیم فایل باز کنیم یا اطلاعات را در فایلی ذخیره کنیم. در PyQt6 این کار به‌سادگی با ویجت **QFileDialog** انجام می‌شود.

---

### مثال: برنامه‌ی ساده برای باز و ذخیره فایل

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Open and Save File Example")
        self.resize(500, 400)

        # Create text editor as central widget
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Create menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        # Create actions
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)

        # Add actions to File menu
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Connect actions
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(self.close)

    def open_file(self):
        # Show open file dialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.editor.setText(f.read())

    def save_file(self):
        # Show save file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
```

---

### توضیح کد

* متد `getOpenFileName` یک پنجره‌ی انتخاب فایل باز می‌کند و مسیر فایل انتخابی را برمی‌گرداند.
* متد `getSaveFileName` مسیر ذخیره فایل را از کاربر می‌گیرد.
* از `QTextEdit` به‌عنوان ویرایشگر متنی استفاده کردیم و متن باز شده را در آن قرار دادیم.
* هنگام ذخیره‌سازی، محتوای داخل `QTextEdit` در فایل نوشته می‌شود.

---

📌 نتیجه:
حالا یک برنامه‌ی کوچک دارید که می‌تواند فایل متنی را باز کند یا آن را ذخیره کند. درست مثل یک **دفترچه یادداشت ساده**. 📝

---

✅ در **صفحه ۷** اولین پروژه‌ی کوچک و کامل خودمان را می‌سازیم: **ماشین حساب ساده** با عملیات جمع، تفریق، ضرب و تقسیم. ➕➖✖️➗

