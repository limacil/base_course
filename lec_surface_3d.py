import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание 3D-пространства
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

# Определение параметров кривой
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)
R = 5
# Параметрическое задание пространственной кривой
x = R * np.outer(np.cos(phi), np.sin(theta))
y = R * np.outer(np.sin(phi), np.sin(theta))
z = R * np.outer(np.ones(np.size(phi)), np.cos(theta))

# Построение пространственной кривой
ax.plot_surface(x, y, z, label='Dich')

# Подписи и масштабирование
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')

# plt.show()
plt.savefig('fig_2.png')