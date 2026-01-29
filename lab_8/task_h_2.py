from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

N = 100

t = np.linspace(0, 16*np.pi, 100)

x = 2**(-0.1*t) * np.cos(2*t)
y = 2**(-0.1*t) * np.sin(2*t)
z = 1 * t

ball, = ax.plot(x, y, z, 'o', color='b')
line, = ax.plot(x, y, z, '-', color='b')


def animate(i):
    ball.set_data([x[i]], [y[i]])
    ball.set_3d_properties(z[i])

    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])


ax.set_xlim3d([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



ani = FuncAnimation(fig, animate, N, interval=30)
# plt.show()
ani.save('task_h_2.gif')