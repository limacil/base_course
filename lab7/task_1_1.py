import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

R = 1  

t = np.linspace(0, 4*np.pi, 200) 

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

fig, ax = plt.subplots()
ax.set_xlim(0, 4*np.pi*R)
ax.set_ylim(0, 2*R)
line, = ax.plot([], [], lw=2)

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=50) 

ani.save('task_1_1.gif', writer="pillow")