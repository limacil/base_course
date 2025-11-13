
import numpy as np
import physics_constants as pc


v0 = 20
alpha = np.deg2rad(45)
g = pc.g

t = np.linspace(0, 8, 81)  # от 0 до 8 секунд с шагом 0.1 с

# Уравнения движения
x = v0 * np.cos(alpha) * t
y = v0 * np.sin(alpha) * t - 0.5 * g * t**2

# Скорость в момент времени t
vx = v0 * np.cos(alpha)
vy = v0 * np.sin(alpha) - g * t

# Объединяем результаты в массив
result = np.vstack((t, x, y, vx * np.ones_like(t), vy)).T

# Выводим первые 5 строк
print("t, x, y, vx, vy:")
print(result[:5])

