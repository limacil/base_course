import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import mpl_toolkits.mplot3d.axes3d as plt3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

N = 100
edge = 20


def animate(t):
    x = 2*np.cos(2*t)
    y = 2 * np.sin(2*t)
    z = -t
    return x, y, z

x, y, z = [], [], []

for i in np.linspace(0, 16*np.pi, N):

    ax.set_xlim3d([-edge, edge])
    ax.set_xlabel('X')
    
    ax.set_ylim3d([-edge, edge])
    ax.set_ylabel('Y')
    
    ax.set_zlim3d([-edge, edge])
    ax.set_zlabel('Z')

    x0, y0, z0 = animate(edge/N*i)
    x.append(x0)
    y.append(y0)
    z.append(z0)
    ax.plot(x, y, z, color='b')
    plt.savefig(f'pic_{i}.png')

images = []
filenames = [f'pic_{i}.png' for i in np.linspace(0, 16*np.pi, N)]

for filename in filenames:
    images.append(imageio.imread(filename))
    os.remove(filename)
imageio.mimsave('task_h_2_n.gif', images)