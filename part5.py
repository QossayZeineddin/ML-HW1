import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd




columns = ["Midterm", "Final"]
df = pd.read_csv("NewGrades.csv", usecols=columns)
x = df.Midterm
y = df.Final
x = np.array(x).reshape(-1,1)
y = np.array(y).reshape(-1,1)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.1)
reg = LinearRegression()
reg.fit(X_train, y_train)
print("W00: ", reg.intercept_)
print("W11: ", reg.coef_)


#
# Themodel = LinearRegression()
# x = np.expand_dims(x, 1)
# Themodel.fit(x,y)
# plt.scatter(x, y)
# f = Themodel.coef_*x + Themodel.intercept_
# plt.plot(x, f, 'r')
# plt.xlabel("Mid")
# plt.ylabel("Final")
# plt.show()

columns = ["Midterm", "Final"]
df = pd.read_csv("NewGrades.csv", usecols=columns)
x = df.Midterm
y = df.Final
x = np.array(x)
y = np.array(y)



Themodel = LinearRegression()
x = np.expand_dims(x, 1)
Themodel.fit(x,y)
print("w1: ", Themodel.coef_)
print("w0: ", Themodel.intercept_)
plt.scatter(x, y)
x = x
f = Themodel.coef_*x + Themodel.intercept_
plt.plot(x, f, 'r')
plt.xlabel("Mid")
plt.ylabel("Final")
plt.show()