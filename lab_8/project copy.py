import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import imageio
import os

N = 50
frame = 0
edge = 40

def animate(R):
    for eta in np.arange(0, 2*np.pi, 0.1):
        x = np.outer(phi, np.cos(theta))
        y = np.outer(phi, np.sin(theta))
        z = np.outer(phi**2, np.ones(len(theta))) * np.sin(eta)
    return x, y, z




for eta in np.arange(0, 2*np.pi, 0.1):
    # Создание 3D-пространства
    fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

    # Определение параметров кривой
    phi = np.linspace(0, 2*np.pi, 100)
    theta = np.linspace(0, 2*np.pi, 100)

    # Параметрическое задание пространственной кривой
    x = np.outer(phi, np.cos(theta))
    y = np.outer(phi, np.sin(theta))
    z = np.outer(phi**2, np.ones(len(theta))) * np.sin(eta)

    # Построение пространственной кривой
    ax.plot_surface(x, y, z, label='Dich')

    # Подписи и масштабирование
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim3d([-edge, edge])
    ax.set_ylim3d([-edge, edge])
    ax.set_zlim3d([-edge, edge])

    ax.set_title('3D Test')

    plt.savefig(f'pic_{i}')

images = []
filenames = [f'pic_{i}.png' for i in range(N)]

for filename in filenames:
    images.append(imageio.imread(filename))
    os.remove(filename)
imageio.mimsave('pro.gif', images)