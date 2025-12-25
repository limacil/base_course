import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def star_move(t, x0=0, y0=0, a=0):
    x = 10 * np.cos(t)**3
    y = 10 * np.sin(t)**3


    X = x0 + (x+10) * np.cos(a) - (y-10) * np.sin(a)
    Y = y0 + (x-10) * np.sin(a) + (y+10) * np.cos(a)

    return X, Y


fig, ax = plt.subplots()

star, = plt.plot([], [], 'y', lw=2)


def animate(i):
    angle = 0.1 * i
    t = np.linspace(0, 2 * np.pi, 500)
    X, Y = star_move(t, x0=0, y0=0, a=angle)
    star.set_data(X, Y)
    return star,
   

ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

ani = FuncAnimation(fig, animate, frames=100, interval=50)
ani.save('task_h_3.gif', writer="pillow")