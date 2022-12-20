import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["Midterm", "Final"]

df = pd.read_csv("NewGrades.csv", usecols=columns)
print("Contents in csv file:", df)

x = df.Midterm
y = df.Final
data = pd.DataFrame([x, y]).T
data.columns = ['x', 'y']

sns.lmplot(x="x", y="y", data=data, order=1 )
plt.ylabel('Final')
plt.xlabel('Mid')
plt.show()