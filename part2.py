import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("NewGrades.csv")
crr = df.corr(method='pearson')
print(crr)

Names = []
Values = []

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
#columns = ["HW1", "Final"]
#columns = ["HW2", "Final"]
#columns = ["Midterm", "Final"]
columns = ["Project", "Final"]

df = pd.read_csv("NewGrades.csv", usecols=columns)
print("Contents in csv file:", df)

#plt.xlabel('HW1')
#plt.xlabel('HW2')
#plt.xlabel('Midterm')
plt.xlabel('Project')

plt.ylabel('Final')

#plt.scatter(df.HW1, df.Final, color='g', s=100)
#plt.scatter(df.HW2, df.Final, color='r', s=100)
#plt.scatter(df.Midterm, df.Final, color='y', s=100)
plt.scatter(df.Project, df.Final, color='c', s=100)

plt.show()



