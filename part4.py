import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

columns = ["Midterm", "Final"]
df = pd.read_csv("NewGrades.csv", usecols=columns)
print("Contents in csv file:", df)
x = df.Midterm
y = df.Final

w1 = 0.1
w0 = 0.01
costs = []
weights = []
prev_error = None
learning_rate = 0.0001
for i in range(10000000):
    predict = (w1 * x) + w0
    err = np.sum((y - predict) ** 2) / 32
    if prev_error and abs(prev_error - err) <= 0.0000001:
        break
    prev_error = err
    costs.append(err)
    weights.append(w1)
    w1_1 = -(2 / 32) * sum(x * (y - predict))
    w0_0 = -(2 / 32) * sum(y - predict)
    w1 = w1 - (learning_rate * w1_1)
    w0 = w0 - (learning_rate * w0_0)

f = w1 * x + w0
print("w1: "  )
print(w1)
print("w0: "  )
print(w0)
plt.scatter(x , y , marker='o', color='red')
plt.plot([min(x), max(x)], [min(f), max(f)])
plt.xlabel("Mid")
plt.ylabel("Final")
plt.show()