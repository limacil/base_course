import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def cikloida_move(R, t):
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    return x, y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
ball_line, = plt.plot([], [], '-', color='r', label='Ball')

frames = 180
coords = np.zeros((frames, 2))


def animate(i):
    coords[i] = cikloida_move(R=2, t=i)
    ball.set_data([coords[i][0]], [coords[i][1]])
    ball_line.set_data(coords[:i, 0], coords[:i, 1])
    return ball, ball_line


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('task_1.gif', writer="pillow")