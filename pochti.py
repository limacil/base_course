import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Координаты
x = np.linspace(-2.5, 2.5, 1000)
y = np.linspace(-2.5, 2.5, 1000)
X, Y = np.meshgrid(x, y)

# Расчёт высоты
R = np.sqrt(X**2 + Y**2)

# Сложный рельеф: основание + склон + кратер + центральный конус
Z = np.zeros_like(R)

# Основание (пологая часть)
mask_base = R <= 2.0
Z[mask_base] = 0.2 * (1 - R[mask_base]/2.0)**2

# Главный конус
mask_cone = (R > 0.5) & (R <= 2.0)
Z[mask_cone] += 0.8 * (1 - (R[mask_cone] - 0.5)/1.5)

# Кратер (углубление)
mask_crater = (R > 0.3) & (R <= 0.8)
Z[mask_crater] = 0.9 - 1.2 * (R[mask_crater] - 0.3)/0.5

# Центральная возвышенность (жерло)
mask_vent = R <= 0.3
Z[mask_vent] = 0.7 + 0.5 * (1 - R[mask_vent]/0.3)

# Сглаживание небольшого шума (по желанию)
from scipy.ndimage import gaussian_filter
Z = gaussian_filter(Z, sigma=0.5)

# Отрисовка
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='terrain', edgecolor='none', 
                       antialiased=True, alpha=0.95)

ax.set_title('Вулкан с кратером и жерлом', fontsize=14, pad=20)
ax.set_xlabel('X координата')
ax.set_ylabel('Y координата')
ax.set_zlabel('Высота')

# Добавляем облако "дыма" из точек
theta = np.random.uniform(0, 2*np.pi, 500)
r = np.random.uniform(0, 0.8, 500)
x_smoke = r * np.cos(theta)
y_smoke = r * np.sin(theta)
z_smoke = np.random.uniform(0.9, 1.4, 500)

ax.scatter(x_smoke, y_smoke, z_smoke, c='gray', alpha=0.3, s=10)

fig.colorbar(surf, ax=ax, shrink=0.6, aspect=20, label='Высота')

plt.savefig('pochti.jpg')