import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание 3D-пространства
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

# Определение параметров кривой
t = np.linspace(0, 16*np.pi, 100)
R=10

# Параметрическое задание пространственной кривой
x = np.outer(R, np.cos(t)**3)
y = np.outer(R, np.sin(t)**3)
z = np.outer(np.cos(2*t), 1)

# Построение пространственной кривой
ax.plot_surface(x, y, z, label='Dich')

# Подписи и масштабирование
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')

# plt.show()
plt.savefig('task_2_3.png')