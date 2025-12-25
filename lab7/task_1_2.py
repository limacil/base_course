import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

R = 4  
t = np.linspace(0, 2*np.pi, 500)  

x = R * np.cos(t)**3
y = R * np.sin(t)**3


fig, ax = plt.subplots()
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)


line, = ax.plot([], [], lw=2)

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,


ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20)

ani.save('task_1_2.gif', writer="pillow")