import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def circle_move(t):
    x0 = 0
    y0 = 0
    x = 12 * np.cos(t) + 8 * np.cos(1,5 * t)
    y = 12 * np.sin(t) + 8 * np.sin(1,5 * t)
    
    a = np.arange(0, 2*np.pi, 0.1)
    
    X = x0 + x * np.cos(a) - y * np.cos(a)
    Y = y0 + y * np.cos(a) + x * np.sin(a)
    return X, Y


fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')


def animate(i):
    ball.set_data(circle_move(t = 0.4 * np.pi, time=i))
    return ball
   

plt.axis('equal')
ax.set_xlim(-25, 25)
ax.set_ylim(-25, 25)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('task_H_3.gif', writer="pillow")