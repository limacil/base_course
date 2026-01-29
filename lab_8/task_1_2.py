import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание 3D-пространства
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

# Определение параметров кривой
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)

# Параметрическое задание пространственной кривой
x = np.outer(phi, np.cos(theta))
y = np.outer(phi, np.sin(theta))
z = np.outer(10, theta)

# Построение пространственной кривой
ax.plot_surface(x, y, z, label='Dich')

# Подписи и масштабирование
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')

# plt.show()
plt.savefig('task_1_2.png')