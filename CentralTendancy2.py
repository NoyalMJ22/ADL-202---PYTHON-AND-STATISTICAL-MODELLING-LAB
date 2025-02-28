import numpy as np
import pandas as pd

classintervals = [(0,10), (10,20), (20,30), (30,40), (40,50), (50,60), (60,70), (70,80)]
frequencies = [5, 10, 20, 40, 30, 20, 10, 5]

df = pd.DataFrame(classintervals, columns=['Lower', 'Upper'])
df['Midpoint'] = (df['Lower'] + df['Upper']) / 2
df['Frequency'] = frequencies

totalfrequency = df['Frequency'].sum()

mean = (df['Frequency'] * df['Midpoint']).sum() / totalfrequency

df['Cumulative Frequency'] = df['Frequency'].cumsum()

N = totalfrequency

median_class_index = df[df['Cumulative Frequency'] >= N / 2].index[0]

L = df.loc[median_class_index, 'Lower']

CF = df.loc[median_class_index - 1, 'Cumulative Frequency'] if median_class_index > 0 else 0

f_median = df.loc[median_class_index, 'Frequency']

h = df.loc[median_class_index, 'Upper'] - df.loc[median_class_index, 'Lower']

median = L + (((N / 2) - CF) / f_median) * h

sum_fX2 = (df['Frequency'] * df['Midpoint']**2).sum()
variance = (sum_fX2 / totalfrequency) - (mean ** 2)

print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Variance: {variance:.2f}")
