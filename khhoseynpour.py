import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x = np.random.rand() برای تولید یک عدد تصادفی بین 0 و 1:
# x = np.random.uniform(3,10,3) برای تولید عدد تصادفی بین دو عدد (a و b):
# x = np.random.randint(3,10,3) برای تولید یک عدد صحیح تصادفی بین دو عدد (a و b):
# x = np.random.rand(5, 6) برای تولید یک آرایه 5 * 6 بعدی از اعداد تصادفی:
# x = np.random.normal(0,1,10)
# x = np.random.uniform(10,20,(4,5))
# print(np.max(x))
# np.random.seed(123)

# data = {
#     'Order ID': [1, 2, 3, 4, 5, 6, 7, 8],
#     'Product': ['Widget A', 'Widget B', 'Widget A', 'Widget C', 'Widget B', 'Widget A', 'Widget C', 'Widget B'],
#     'Quantity': [4, 2, 1, 5, 3, 2, 1, 4],
#     'Price per Unit': [10, 15, 10, 20, 15, 10, 20, 15],
#     'Total Sales': [40, 30, 10, 100, 45, 20, 20, 60],
#     'Date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08'])
# }


# start_date = '2024-01-01'
# end_date = '2024-01-05'

# df = pd.DataFrame(data)
# av = df["Product"].value_counts()
# # av2 = df.groupby("Product")["Price per Unit"].sum()
# # av = df[(df["Date"]>start_date) & (df["Date"] < end_date)]
# print(av)
# # x = df.groupby("Product")["Quantity"].sum()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def fitness_function(features, X_train, X_test, y_train, y_test):
    selected_features = [i for i in range(len(features)) if features[i] == 1]
    if len(selected_features) == 0:
        return 0  # جلوگیری از انتخاب هیچ ویژگی
    X_train_sel = X_train[:, selected_features]
    X_test_sel = X_test[:, selected_features]
    model = RandomForestClassifier()
    model.fit(X_train_sel, y_train)
    y_pred = model.predict(X_test_sel)
    return accuracy_score(y_test, y_pred)


def pso(X, y, num_particles, max_iter):
    num_features = X.shape[1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    particles = np.random.randint(2, size=(num_particles, num_features))
    velocities = np.random.uniform(-1, 1, (num_particles, num_features))
    pbest = particles.copy()
    pbest_scores = np.zeros(num_particles)
    for i in range(num_particles):
        pbest_scores[i] = fitness_function(particles[i], X_train, X_test, y_train, y_test)
    gbest = particles[np.argmax(pbest_scores)]
    gbest_score = max(pbest_scores)
    omega = 0.5  # ضریب اینرسی
    c1 = c2 = 2  # ضرایب یادگیری
    
    for _ in range(max_iter):
        for i in range(num_particles):
            # به‌روزرسانی سرعت
            r1, r2 = np.random.rand(), np.random.rand()
            velocities[i] = omega * velocities[i] + c1 * r1 * (pbest[i] - particles[i]) + c2 * r2 * (gbest - particles[i])
            velocities[i] = np.clip(velocities[i], -1, 1)  # محدود کردن سرعت
            # به‌روزرسانی موقعیت
            particles[i] = np.where(np.random.rand(num_features) < 1 / (1 + np.exp(-velocities[i])), 1, 0)
            x = omega * velocities[i]
            y = c1 * r1 * (pbest[i] - particles[i])
            # print(f"سرعت قبلی {x}")
            # print(f"تأثیر بهترین موقعیت فردی {y}")
            # print(f"تأثیر بهترین موقعیت گروهی {(c2 * r2 * (gbest - particles[i]))} محاسبه می‌شود.")
            fitness = fitness_function(particles[i], X_train, X_test, y_train, y_test)
            if fitness > pbest_scores[i]:
                pbest[i] = particles[i]
                pbest_scores[i] = fitness
                if fitness > gbest_score:
                    gbest = particles[i]
                    gbest_score = fitness
    
    return gbest, gbest_score

# Generate synthetic data and run PSO
if __name__ == "__main__":
    X, y = make_classification(n_samples=500, n_features=20, n_informative=15, random_state=42)
    best_features, best_score = pso(X, y, num_particles=30, max_iter=50)
    print("Best Features:", best_features)
    print("Best Accuracy:", best_score)
