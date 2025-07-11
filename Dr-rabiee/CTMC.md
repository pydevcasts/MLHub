

فرض کنید یک مرکز تلفن با **۲ خط (m = 2)** داریم. نرخ ورود تماس‌ها:

* $\lambda = 5$ تماس در دقیقه
  و نرخ سرویس:
* $\mu = 3$ تماس در دقیقه برای هر خط مشغول.

### خواسته‌ها:

**الف)** فضای حالت سیستم را بنویسید.
**ب)** معادلات توازن سراسری (GBE) را بنویسید.
**ج)** احتمال اشغال کامل خطوط (یعنی $P_{\text{block}} = \pi_2$) را حساب کنید.

---

## ✅ پاسخ:

### 🔹 الف) فضای حالت

تعداد خطوط اشغال‌شده ممکن است بین 0 تا 2 باشد. پس:

$$
S = \{0, 1, 2\}
$$

---

### 🔹 ب) معادلات توازن سراسری (GBE)

در حالت پایدار، جریان ورودی به هر حالت برابر است با جریان خروجی از آن.

---

#### 🔸 حالت 0:

ورودی: از حالت 1 با نرخ $\mu = 3$
خروجی: به حالت 1 با نرخ $\lambda = 5$

$$
\pi_1 \cdot \mu = \pi_0 \cdot \lambda
\Rightarrow 3\pi_1 = 5\pi_0 \tag{1}
$$

---

#### 🔸 حالت 1:

ورودی: از حالت 0 با نرخ $\lambda = 5$، از حالت 2 با نرخ $2\mu = 6$
خروجی: به حالت 0 با نرخ 3، به حالت 2 با نرخ 5

$$
\pi_0 \cdot \lambda + \pi_2 \cdot 2\mu = \pi_1 \cdot (\lambda + \mu)
\Rightarrow 5\pi_0 + 6\pi_2 = 8\pi_1 \tag{2}
$$

---

#### 🔸 حالت 2:

ورودی: از حالت 1 با نرخ $\lambda = 5$
خروجی: به حالت 1 با نرخ $2\mu = 6$

$$
\pi_1 \cdot \lambda = \pi_2 \cdot 2\mu
\Rightarrow 5\pi_1 = 6\pi_2 \tag{3}
$$

---

#### 🔸 شرط نرمال‌سازی:

$$
\pi_0 + \pi_1 + \pi_2 = 1 \tag{4}
$$

---

### 🔹 ج) حل معادلات برای پیدا کردن $\pi_2$

از (1):

$$
\pi_1 = \frac{5}{3} \pi_0
$$

از (3):

$$
\pi_2 = \frac{5}{6} \pi_1 = \frac{5}{6} \cdot \frac{5}{3} \pi_0 = \frac{25}{18} \pi_0
$$

حالا در (4) جایگذاری کنیم:

$$
\pi_0 + \pi_1 + \pi_2 = 1  
\Rightarrow \pi_0 + \frac{5}{3}\pi_0 + \frac{25}{18}\pi_0 = 1
$$

هم‌مخرج:

$$
\pi_0 \left(1 + \frac{5}{3} + \frac{25}{18}\right) = 1  
\Rightarrow \pi_0 \cdot \frac{18 + 30 + 25}{18} = 1  
\Rightarrow \pi_0 \cdot \frac{73}{18} = 1  
\Rightarrow \pi_0 = \frac{18}{73}
$$

---

حالا:

$$
\pi_1 = \frac{5}{3} \cdot \frac{18}{73} = \frac{30}{73}, \quad
\pi_2 = \frac{25}{18} \cdot \frac{18}{73} = \frac{25}{73}
$$

---

### 🎯 نتیجه نهایی:

* $\pi_0 = \frac{18}{73} \approx 0.2466$
* $\pi_1 = \frac{30}{73} \approx 0.4110$
* $\pi_2 = \frac{25}{73} \approx 0.3425$

---

### ✅ پاسخ بخش (ج):

احتمال انسداد تماس جدید = **احتمال اشغال کامل خطوط** =

$$
\boxed{P_{\text{block}} = \pi_2 = \frac{25}{73} \approx 34.25\%}
$$

---
