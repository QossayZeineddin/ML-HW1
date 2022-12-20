import csv
import pandas as pd
from collections import Counter

column_totals = Counter()
with open("grades.csv", "r") as f:
    reader = csv.reader(f)
    row_count = 0.0
    for row in reader:
        for column_idx, column_value in enumerate(row):
            try:
                if(column_value.isdigit()):
                    n = float(column_value)
                    if (n != 0):
                        column_totals[column_idx] += n
            except ValueError:
                print("Error -- ({}) Column({}) could not be converted to float!".format(column_value, column_idx))
        row_count += 1.0

# row_count is now 1 too many so decrement it back down
row_count -= 1.0
# make sure column index keys are in order
column_indexes = column_totals.keys()
sorted(column_indexes)

# calculate per column averages using a list comprehension and casces it to Intger
averages = [int(column_totals[idx] / row_count) for idx in column_indexes]
print(averages)

df = pd.read_csv("grades.csv")
df['HW1'] = df['HW1'].replace({0: averages[0]})
df['HW2'] = df['HW2'].replace({0: averages[1]})
df['Midterm'] = df['Midterm'].replace({0: averages[2]})
df['Project'] = df['Project'].replace({0: averages[3]})
df['Final'] = df['Final'].replace({0: averages[4]})
df.to_csv("NewGrades.csv", index=False)
print("All 0 value fill with it's average")




