import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_trap(nb, ax):
    h = 2/nb
    for i in range(nb):
        x_0 = 2 + i * h
        x_1 = 2 + (i + 1) * h
        
        patch = patches.Polygon(
            list(zip([x_0, x_0, x_1, x_1],
                     [0, x_0**3, x_1**3, 0])),
            closed=True, fill=None, color="red", linewidth=2)
        ax.add_patch(patch)
    
x = np.linspace(1, 5, 200)
y = x ** 3

graphe, ax = plt.subplots(2, 1)
ax[0].plot(x, y)
ax[0].set_xlabel("x")
ax[0].set_ylabel("f(x)")
draw_trap(3, ax[0])

ax[1].plot(x, y)
ax[1].set_xlabel("x")
ax[1].set_ylabel("f(x)")
draw_trap(12, ax[1])


plt.show()

