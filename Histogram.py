import matplotlib.pyplot as plt
import numpy as np

bins = [135, 140, 145, 150, 155]
students = [12, 16, 18, 14]

plt.hist(bins[:-1], bins=bins, weights=students, color='lightcyan', edgecolor='black')
plt.title("Histogram of Student Heights")
plt.xlabel("Height of Students")
plt.ylabel("Number of Students")
plt.yticks(np.arange(0,20,5))
plt.show()
