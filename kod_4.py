import numpy as np
import matplotlib.pyplot as plt

# сетка
x = np.linspace(1, 100, 200)
z = np.linspace(0, 50, 100)
X, Z = np.meshgrid(x, z)

# параметры
q = 10      # мощность источника
u = 2       # ветер
h = 20      # высота
sigma_z = 0.1 * X
sigma_y = 0.1 * X

# чтобы не делить на 0
sigma_z[sigma_z == 0] = 1
sigma_y[sigma_y == 0] = 1

# формула
C = (q / (2 * np.pi * sigma_y * sigma_z * u)) * (
    np.exp(-(Z - h)**2 / sigma_z**2) +
    np.exp(-(Z + h)**2 / sigma_z**2)
)

# график
plt.imshow(C, origin='lower', aspect='auto')
plt.colorbar(label="Концентрация")
plt.title("Гауссов шлейф")
plt.xlabel("x")
plt.ylabel("z")
plt.savefig("kod_4.png")

