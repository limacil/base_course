import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание 3D-пространства
fig, ax = plt.subplots(subplot_kw={"projection":"3d"})

# Определение параметров кривой
t = np.arange(0, 16*np.pi, 0.01)


# Параметрическое задание пространственной кривой
x = np.outer(2**(-0.1*t), np.cos(2*t))
y = np.outer(2**(-0.1*t), np.sin(2*t))
z = np.outer(-1, t)

# Построение пространственной кривой
ax.plot_surface(x, y, z, label='Dich')

# Подписи и масштабирование
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('3D Test')

# plt.show()
plt.savefig('task_2_2.png')