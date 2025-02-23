import matplotlib.pyplot as plt

x=np.arange(6)
y = x**4 + 5

plt.plot(x, y, label="y = x^4 + 5", color='blue')
plt.title("Graph of y = x^4 + 5")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()
