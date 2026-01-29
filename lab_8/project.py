import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import mpl_toolkits.mplot3d.axes3d as plt3d

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

N = 100
edge = 20
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, 2*np.pi, 100)
i = np.linspace(1, 0, N)


def animate(i):
    x = phi, np.cos(theta)
    y = phi, np.sin(theta)
    z = phi**2, np.ones(len(theta)) * i
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
imageio.mimsave('project.gif', images)