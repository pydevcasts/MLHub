import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# # # data = {
# # #     "A":[1,1,2,2],
# # #     "B":[2.5,3.5,4.0,5.0]
# # # }

# # # df = pd.DataFrame(data)

# # # x = df.groupby("A")["B"].mean().reset_index()
# # # x.columns = ["Siya", "mak"]
# # # print(x)
# # # =======================================
# data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
#                {'a': 100, 'b': 200, 'c': 300, 'd': 400},
#               {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
# df = pd.DataFrame(data)
# # # # x = df["Name"].idxmax()
# # # y = {"Name":df.loc[1, "Name"], "Score":df.loc[2, "Score"], "Age":df.iloc[0]}
# # # p = df.loc[0:,"Price"]
# # # t = p["Quantity"] * p["Price"]
# # # x = df.groupby("Product")[t].sum()
# # print(p)
# # x = df.iloc[1:3]
# # x = df.loc[0, "b"]
# print(df)

x = np.linspace(0, 3, 16)
print(x)
y = x ** 2

plt.plot(x, y)
plt.show()


