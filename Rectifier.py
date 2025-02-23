import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 500)
inputsignal = np.sin(t)

outputsignal = np.abs(inputsignal)

plt.plot(t, inputsignal, label="Input Signal (Sine Wave)", color="blue")
plt.plot(t, outputsignal, label="Full-Wave Rectified Output", color="red", linestyle="--")
plt.title("Full-Wave Rectifier")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
