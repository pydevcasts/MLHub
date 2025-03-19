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


