import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3D
import math

from numpy import linspace

x = linspace(0, 5, 20)

fig, ax = plt.subplots(facecolor='w', edgecolor='k')
ax.plot(x, math.sin(x), marker="o", color="r", linestyle="None")

ax.grid(True)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
ax.legend(["y = x**2"])

plt.title("Puntos")
plt.show()