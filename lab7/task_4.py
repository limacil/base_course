import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fractal_points(x0, y0, C, D, n):
    
    x = np.zeros(n)
    y = np.zeros(n)
    x[0] = x0
    y[0] = y0
    for i in range(1, n):
        x[i] = x[i - 1] ** 2 - y[i - 1] ** 2 + C
        y[i] = 2 * x[i - 1] * y[i - 1] + D
    return x, y

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
n = 200

x1, y1 = fractal_points(x0, y0, C, D, n)

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)


scatter, = ax.plot([], [], "bo", markersize=5)


def animate(i):
    
    scatter.set_data(x1[:i], y1[:i])
    return scatter,

ani = animation.FuncAnimation(fig, animate, frames=n, interval=50)

ani.save('task_4.gif', writer="pillow")