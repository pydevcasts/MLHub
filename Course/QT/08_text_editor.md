## صفحه ۸ – پروژه دفترچه یادداشت ساده (Text Editor) 📝

در این پروژه از ویجت **QTextEdit** برای نوشتن متن استفاده می‌کنیم و با کمک **QFileDialog** امکان باز و ذخیره فایل را فراهم می‌کنیم. همچنین یک منوی ساده برای مدیریت عملیات ایجاد می‌کنیم.

---

### کد پروژه

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Simple Text Editor")
        self.resize(600, 400)

        # Create text editor
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        # Create menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        # Create actions
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        clear_action = QAction("Clear", self)
        exit_action = QAction("Exit", self)

        # Add actions to menu
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(clear_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        # Connect actions
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        clear_action.triggered.connect(self.clear_text)
        exit_action.triggered.connect(self.close)

    def open_file(self):
        # Open file dialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "r", encoding="utf-8") as f:
                self.editor.setText(f.read())

    def save_file(self):
        # Save file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.editor.toPlainText())

    def clear_text(self):
        # Clear editor content
        self.editor.clear()

app = QApplication(sys.argv)
window = TextEditor()
window.show()
sys.exit(app.exec())
```

---

### توضیح کد

* `QTextEdit` یک ویجت چند خطی برای نوشتن و ویرایش متن است.
* از **منوی File** برای مدیریت عملیات استفاده کردیم: باز کردن، ذخیره کردن، پاک کردن متن و خروج.
* اکشن "Clear" محتوای ادیتور را خالی می‌کند.
* فایل‌های متنی با انکدینگ UTF-8 باز و ذخیره می‌شوند.

---

📌 نتیجه:
حالا یک دفترچه یادداشت ساده دارید که می‌تواند متن را ویرایش کند، در فایل ذخیره کند و دوباره باز کند. درست مثل یک **نوت‌پد کوچک**. ✨

---

✅ در **صفحه ۹** به سراغ ویجت‌های پیشرفته‌تر می‌رویم مثل **تقویم (QCalendarWidget) 📅، اسلایدر (QSlider) 🎚️ و ProgressBar 🔄** که در خیلی از نرم‌افزارهای حرفه‌ای کاربرد دارند.

