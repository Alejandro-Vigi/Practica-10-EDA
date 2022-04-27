import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(0, 4, 0.05)
x = np.linspace(0,5,20)
y = np.sin(x*np.pi)

fig, ax = plt.subplots(figsize=(3,2), constrained_layout=True, facecolor='w', edgecolor='k')
ax.plot(x, np.sin(x), marker="o", color="r", linestyle="None")
ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)
ax.legend(["y = sen(x)"])
ax.set_title('Seno x ')
#fig.set_facecolor('lightsteelblue')

plt.show()
fig.savefig("Grafica.png")