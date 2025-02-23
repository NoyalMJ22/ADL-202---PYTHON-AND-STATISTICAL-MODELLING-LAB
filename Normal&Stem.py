import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.sin(x)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(x, y, label="Normal Graph", color="blue")
plt.title("Normal Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.subplot(1, 2, 2)
plt.stem(x, y, linefmt='green', markerfmt='.', basefmt='black', label="Stem Graph")
plt.title("Stem Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()

plt.show()
