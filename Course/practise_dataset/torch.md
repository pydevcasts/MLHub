#### مقدمه‌ای بر پای‌تورچ

#### 1. نصب پای‌تورچ

برای شروع، ابتدا باید پای‌تورچ را نصب کنید. می‌توانید از دستور زیر برای نصب آن استفاده کنید:

```bash
pip install torch torchvision torchaudio
```

#### 2. آشنایی با تنسورها (Tensors)

تنسورها ساختارهای داده‌ای اصلی در پای‌تورچ هستند. آن‌ها شبیه به آرایه‌ها در NumPy هستند، اما با قابلیت‌های بیشتری. 

#### انواع تنسورها

- **تنسور یک بعدی**: مشابه لیست‌ها.
- **تنسور دو بعدی**: مشابه ماتریس‌ها.
- **تنسور سه بعدی**: مشابه آرایه‌های چند بعدی.

#### ایجاد تنسور

```python
import torch

# ایجاد یک تنسور یک بعدی
tensor_1d = torch.tensor([1, 2, 3, 4])
print(tensor_1d)

# ایجاد یک تنسور دو بعدی
tensor_2d = torch.tensor([[1, 2], [3, 4]])
print(tensor_2d)

# ایجاد یک تنسور سه بعدی
tensor_3d = torch.tensor([[[1], [2]], [[3], [4]]])
print(tensor_3d)
```

#### 3. ویژگی‌های مهم تنسورها

#### 3.1. نوع داده (Data Type)

تنسورها می‌توانند انواع مختلف داده‌ها (مانند `float`, `int`, `double` و ...) را داشته باشند. می‌توانید نوع داده را به صورت زیر تغییر دهید:

```python
tensor_float = torch.tensor([1, 2, 3], dtype=torch.float32)
print(tensor_float)
```

#### 3.2. ابعاد (Shape)

ابعاد تنسور را می‌توان با استفاده از ویژگی `shape` مشاهده کرد:

```python
print(tensor_2d.shape)  # خروجی: torch.Size([2, 2])
```

#### 3.3. دستگاه (Device)

تنسورها می‌توانند بر روی CPU یا GPU قرار بگیرند. برای انتقال تنسور به GPU از متد `to` استفاده می‌شود:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor_gpu = tensor_2d.to(device)
print(tensor_gpu.device)
```

#### 4. عملیات ریاضی بر روی تنسورها

پای‌تورچ به شما این امکان را می‌دهد که عملیات ریاضی مختلفی روی تنسورها انجام دهید. این عملیات شامل جمع، ضرب و دیگر عملیات ریاضی است:

```python
a = torch.tensor([[1, 2], [3, 4]])
b = torch.tensor([[5, 6], [7, 8]])

# جمع دو تنسور
sum_tensor = a + b

# ضرب دو تنسور
product_tensor = a * b

print(sum_tensor)
print(product_tensor)
```

#### 5. ساخت مدل‌های یادگیری عمیق

#### 5.1. تعریف یک مدل

مدل‌های شبکه عصبی در پای‌تورچ با استفاده از کلاس `nn.Module` تعریف می‌شوند. به عنوان مثال، یک مدل ساده می‌تواند به شکل زیر باشد:

```python
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(2, 2)  # لایه ورودی به خروجی

    def forward(self, x):
        return self.fc1(x)

model = SimpleNN()
```

#### 5.2. معیار و بهینه‌ساز

برای آموزش مدل، به یک معیار (Loss Function) و یک بهینه‌ساز (Optimizer) نیاز دارید:

```python
criterion = nn.MSELoss()  # معیار خطای میانگین مربعات
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # بهینه‌ساز گرادیان نزولی
```

#### 5.3. آموزش مدل

آموزش مدل شامل مراحل زیر است:

1. پیش‌بینی خروجی با استفاده از داده‌های ورودی.
2. محاسبه خطا.
3. محاسبه گرادیان‌ها.
4. به‌روزرسانی وزن‌ها.


```python

inputs = torch.tensor([[1.0, 2.0], [3.0, 4.0]]) # داده‌های ورودی و هدف
targets = torch.tensor([[1.0, 0.0], [0.0, 1.0]])


for epoch in range(100): # آموزش مدل
    optimizer.zero_grad()  # صفر کردن گرادیان‌ها
    outputs = model(inputs)  # پیش‌رو
    loss = criterion(outputs, targets)  # محاسبه خطا
    loss.backward()  # محاسبه گرادیان‌ها
    optimizer.step()  # به‌روزرسانی وزن‌ها

print("مدل آموزش داده شده:", model(inputs))
```

#### 6. ذخیره و بارگذاری مدل

برای ذخیره و بارگذاری مدل‌ها می‌توانید از متدهای `torch.save` و `torch.load` استفاده کنید:


```python

torch.save(model.state_dict(), 'model.pth') # ذخیره مدل


model_loaded = SimpleNN()
model_loaded.load_state_dict(torch.load('model.pth')) # بارگذاری مدل
```

تابع `torch.rand` در پای‌تورچ برای ایجاد تنورهای تصادفی با مقادیر از توزیع یکنواخت (Uniform Distribution) بین 0 و 1 استفاده می‌شود. این تابع بسیار مفید است، به‌ویژه در مراحل اولیه ایجاد مدل‌های یادگیری عمیق و هنگام نیاز به داده‌های تصادفی.

### 1. استفاده از `torch.rand`

#### 1.1. ایجاد تنسور تصادفی

شما می‌توانید با استفاده از `torch.rand` تنسورهای تصادفی با ابعاد مختلف ایجاد کنید. به عنوان مثال:

```python
import torch

# ایجاد یک تنسور تصادفی یک بعدی با 5 عنصر
tensor_1d = torch.rand(5)
print("تنسور 1 بعدی تصادفی:", tensor_1d)

# ایجاد یک تنسور تصادفی دو بعدی با ابعاد 3x2
tensor_2d = torch.rand(3, 2)
print("تنسور 2 بعدی تصادفی:\n", tensor_2d)

# ایجاد یک تنسور تصادفی سه بعدی با ابعاد 2x3x4
tensor_3d = torch.rand(2, 3, 4)
print("تنسور 3 بعدی تصادفی:\n", tensor_3d)
```

### 2. ویژگی‌های `torch.rand`

#### 2.1. ابعاد تنسور

با استفاده از `torch.rand`، می‌توانید تنسورهایی با ابعاد مختلف ایجاد کنید. تعداد ورودی‌هایی که به این تابع می‌دهید، به عنوان ابعاد تنسور شناخته می‌شود.

#### 2.2. نوع داده

به طور پیش‌فرض، تنسورهای ایجاد شده با `torch.rand` از نوع `float32` هستند. اگر به نوع دیگری از داده نیاز دارید، می‌توانید از `torch.rand` با پارامتر `dtype` استفاده کنید:

```python

tensor_int = torch.rand(3, dtype=torch.int) #ایجاد یک تنسور تصادفی با نوع داده int
print("تنسور تصادفی با نوع int:", tensor_int) # توجه داشته باشید که این ممکن است نتایج غیرمنتظره‌ای بدهد

```

**نکته:** استفاده از `dtype=torch.int` ممکن است مقادیر صحیحی را ایجاد نکند، زیرا `torch.rand` برای تولید اعداد اعشاری طراحی شده است. برای ایجاد اعداد صحیح، بهتر است از روش‌های دیگری استفاده کنید.

### 3. انتقال تنسور به GPU

اگر می‌خواهید تنسور تصادفی را به GPU منتقل کنید (در صورتی که GPU در دسترس باشد)، می‌توانید از متد `to` استفاده کنید:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor_gpu = torch.rand(3, 2).to(device)
print("تنسور تصادفی بر روی GPU:", tensor_gpu.device)
```



### 1. استفاده از `torch.view`

#### 1.1. تغییر ابعاد یک تنسور

برای استفاده از `torch.view`، باید ابعاد جدید را به عنوان آرگومان به آن بدهید. به عنوان مثال:

```python
import torch

# ایجاد یک تنسور 1 بعدی
tensor_1d = torch.tensor([1, 2, 3, 4, 5, 6])
print("تنسور 1 بعدی:", tensor_1d)

# تغییر ابعاد به 2 بعدی (3 سطر و 2 ستون)
tensor_2d = tensor_1d.view(3, 2)
print("تنسور 2 بعدی:\n", tensor_2d)
```

در مثال بالا، ما یک تنسور 1 بعدی با 6 عنصر داریم و آن را به یک تنسور 2 بعدی با 3 سطر و 2 ستون تغییر داده‌ایم.

### 2. ویژگی‌های `torch.view`

#### 2.1. ابعاد جدید

- ابعاد جدید باید با تعداد کل عناصر تنسور اصلی مطابقت داشته باشد. به عبارت دیگر، حاصل‌ضرب ابعاد جدید باید برابر با تعداد کل عناصر تنسور اصلی باشد. اگر این شرط برقرار نباشد، یک خطا دریافت خواهید کرد.

```python

tensor_3d = tensor_1d.view(2, 3)  # 2 سطر و 3 ستون
print("تنسور 2 بعدی دیگر:\n", tensor_3d) ## این کار درست است

# tensor_error = tensor_1d.view(4, 2)  # Uncommenting this will raise an error # این کار خطا می‌دهد (چون 4 * 2 = 8 != 6)
```

#### 2.2. استفاده از `-1`

شما می‌توانید از `-1` به عنوان یک ابعاد استفاده کنید تا پای‌تورچ به طور خودکار ابعاد مناسب را محاسبه کند. این ویژگی می‌تواند بسیار مفید باشد.

```python
# استفاده از -1 برای محاسبه ابعاد خودکار
tensor_auto = tensor_1d.view(-1, 2)  # تعداد سطرها به طور خودکار محاسبه می‌شود
print("تنسور با ابعاد خودکار:\n", tensor_auto)
```

### 3. حفظ داده‌ها

مهم است بدانید که `torch.view` تنها ابعاد تنسور را تغییر می‌دهد و داده‌ها را تغییر نمی‌دهد. به عبارت دیگر، داده‌های موجود در تنسور اصلی به همان صورت در تنور جدید نیز وجود خواهند داشت.

### 4. انتقال تنسور به GPU

اگر تنسور شما در GPU قرار دارد، می‌توانید از `view` برای تغییر ابعاد آن نیز استفاده کنید:

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tensor_gpu = tensor_1d.to(device)

# تغییر ابعاد تنسور در GPU
tensor_gpu_view = tensor_gpu.view(3, 2)
print("تنسور 2 بعدی در GPU:\n", tensor_gpu_view)
```

در پای‌تورچ، توابع تبدیل (Transforms) عمدتاً در کتابخانه `torchvision` برای پردازش و تبدیل تصاویر استفاده می‌شوند. این توابع به شما این امکان را می‌دهند که داده‌های ورودی خود را پیش‌پردازش کنید و آن‌ها را به فرمت مناسب برای آموزش مدل‌های یادگیری عمیق تبدیل کنید.

### 1. نصب کتابخانه torchvision

اگر هنوز `torchvision` را نصب نکرده‌اید، می‌توانید با استفاده از دستور زیر آن را نصب کنید:

```bash
pip install torchvision
```

### 2. استفاده از توابع تبدیل (Transforms)

کتابخانه `torchvision.transforms` شامل مجموعه‌ای از توابع است که می‌توانید برای آماده‌سازی داده‌های تصویری استفاده کنید. در اینجا به بررسی چند تابع تبدیل محبوب می‌پردازیم:

#### 2.1. وارد کردن کتابخانه

ابتدا باید کتابخانه `torchvision.transforms` را وارد کنید:

```python
import torchvision.transforms as transforms
```

#### 2.2. تغییر اندازه (Resize)

تبدیل اندازه تصویر به ابعاد مشخص:

```python
transform_resize = transforms.Resize((256, 256))
```

#### 2.3. برش (Crop)

برش قسمت مشخصی از تصویر:

```python
transform_crop = transforms.CenterCrop(224)  # برش از مرکز
```

#### 2.4. تغییر به Tensor

تبدیل تصویر PIL به تنسور:

```python
transform_to_tensor = transforms.ToTensor()
```

#### 2.5. نرمال‌سازی (Normalization)

نرمال‌سازی تصویر با مقادیر میانگین و انحراف معیار مشخص:

```python
transform_normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
```

### 3. ترکیب توابع تبدیل

شما می‌توانید چندین تبدیل را در یک پیکربندی ترکیب کنید. به عنوان مثال، برای ایجاد یک مجموعه تبدیل می‌توانید از `transforms.Compose` استفاده کنید:

```python
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.RandomHorizontalFlip(),  # چرخش تصادفی تصویر
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
```

### 4. استفاده از تبدیل‌ها با DataLoader

به‌طور معمول، این تبدیل‌ها در زمان بارگذاری داده‌ها به وسیله `DataLoader` استفاده می‌شوند. به عنوان مثال:

```python
from torchvision import datasets
from torch.utils.data import DataLoader


dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform) #بارگذاری مجموعه داده CIFAR-10 با تبدیل‌ها
dataloader = DataLoader(dataset, batch_size=32, shuffle=True) #حلقه برای مشاهده داده‌ها
#

for images, labels in dataloader:
    print(images.size(), labels.size())
    break  # فقط یک دسته از داده‌ها را مشاهده کنید
```

