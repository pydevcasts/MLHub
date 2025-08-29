
---

### 🔹 مرحله ۱: پایه‌های لازم (Fundamentals)

#### ۱. برنامه‌نویسی
- **پایتون (Python)**: زبان اصلی در بیوانفورماتیک و هوش مصنوعی.
  - متغیرها، حلقه‌ها، شرط‌ها
  - توابع، کلاس‌ها (شی‌گرایی)
  - کار با کتابخانه‌های علمی: `NumPy`, `Pandas`, `Matplotlib`, `Seaborn`
- کار با فایل‌های بیولوژیکی: FASTA, FASTQ, BAM, VCF
- کار با کتابخانه‌های بیوانفورماتیک: `Biopython`

> 💡 تمرین: تحلیل توالی DNA، شمارش نوکلئوتیدها، تبدیل به RNA/پروتئین، یافتن ژن‌ها

---

#### ۲. ریاضیات و آمار
- **آمار و احتمالات**: توزیع‌ها، آزمون فرض، p-value، FDR، معنی‌داری آماری
- **جبر خطی**: بردارها، ماتریس‌ها، ضرب ماتریسی، ویژه‌مقدارها — مهم برای یادگیری ماشین
- **حسابان (Calculus)**: مشتق، گرادیان — برای درک بهینه‌سازی در مدل‌های AI

---

### 🔹 مرحله ۲: یادگیری ماشین (Machine Learning)

#### ۳. مفاهیم پایه یادگیری ماشین
- تفاوت یادگیری نظارت‌شده، نظارت‌نشده، تقویتی
- تقسیم داده: train/test/validation
- Overfitting و Regularization
- ارزیابی مدل: دقت، recall، F1-score، AUC-ROC

#### ۴. الگوریتم‌های کلیدی
- Regression (Linear, Logistic)
- Decision Trees, Random Forest
- Support Vector Machines (SVM)
- Clustering (K-Means, Hierarchical)
- PCA و تحلیل مؤلفه‌های اصلی (برای کاهش ابعاد داده‌های ژنومی)
- Neural Networks مقدماتی (Perceptron, MLP)

> 🛠️ ابزار: `scikit-learn` در پایتون

---

### 🔹 مرحله ۳: هوش مصنوعی پیشرفته (Deep Learning)

#### ۵. شبکه‌های عصبی عمیق
- Dense layers, activation functions (ReLU, sigmoid)
- Backpropagation و بهینه‌سازی (SGD, Adam)
- Dropout, Batch Normalization

#### ۶. شبکه‌های خاص برای داده‌های بیولوژیکی
- **CNN (Convolutional Neural Networks)**: برای تشخیص الگوهای محلی در توالی DNA/RNA
- **RNN / LSTM / GRU**: برای داده‌های توالی‌محور (مثل توالی ژنی، RNA-seq)
- **Transformers**: برای مدل‌سازی طولانی‌مدت (مثل در مدل‌های پیش‌بینی اسپلایسینگ)

> 🛠️ ابزار: `TensorFlow` یا `PyTorch`

---

### 🔹 مرحله ۴: کاربرد در بیوانفورماتیک و ژنتیک

#### ۷. تحلیل داده‌های ژنومی با AI
- پیش‌بینی اگزون/اینtron با مدل‌های ML
- تشخیص جهش‌های پاتوژنیک (pathogenic variants)
- پیش‌بینی بیان ژن (Gene Expression) با شبکه‌های عصبی
- eQTL analysis با مدل‌های آماری و ML

#### ۸. Single-cell RNA-seq analysis
- Clustering سلول‌ها با UMAP/t-SNE
- استفاده از مدل‌های deep learning برای طبقه‌بندی سلول‌ها
- Trajectory inference با مدل‌های پویا

#### ۹. پیش‌بینی ساختار پروتئین
- معرفی AlphaFold و RoseTTAFold
- کار با مدل‌های pre-trained برای پیش‌بینی ساختار

#### ۱۰. Genomic Variant Interpretation
- استفاده از مدل‌هایی مثل DeepSEA, Enformer برای پیش‌بینی اثر جهش‌ها روی تنظیم ژن

---
