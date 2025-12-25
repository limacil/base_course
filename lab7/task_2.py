import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

alpha = 1
t = np.linspace(0, 10, 100)

phi = np.linspace(0, 2 * np.pi, 100)

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
circle = plt.plot([],[])

def update(frame):
    r = alpha * t[frame]
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    circle.set_data(x, y)
    return circle

ani = FuncAnimation(fig, update, frames=len(t), interval=50)
ani.save('task_2.gif', writer="pillow")
