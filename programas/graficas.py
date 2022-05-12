import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import linspace

x = linspace(0, 5, 20)
y = np.sin(x)
fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, y, marker="o", color="r", linestyle="None")

ax.grid(True)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
ax.legend(["y = x**2"])

plt.title("Puntos")
plt.show()