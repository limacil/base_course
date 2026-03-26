import numpy as np
import matplotlib.pyplot as plt

# Параметры сетки
Nx, Nz = 100, 50
dx, dz = 1.0, 1.0
dt = 0.1
steps = 300

# Физические параметры
u = 2.0       # скорость ветра (по x)
vs = 0.5      # скорость осаждения
K = 0.1       # диффузия

# Поле концентрации
C = np.zeros((Nx, Nz))

# Источник (вулкан)
source_x = 10
source_z = Nz - 2

def add_source(C):
    C[source_x, source_z] += 5.0

# Основной цикл
for t in range(steps):
    C_new = C.copy()

    for i in range(1, Nx-1):
        for k in range(1, Nz-1):

            # Перенос (upwind)
            adv_x = -u * (C[i, k] - C[i-1, k]) / dx
            adv_z = vs * (C[i, k+1] - C[i, k]) / dz

            # Диффузия
            diff = K * (
                (C[i+1, k] - 2*C[i, k] + C[i-1, k]) / dx**2 +
                (C[i, k+1] - 2*C[i, k] + C[i, k-1]) / dz**2
            )

            C_new[i, k] = C[i, k] + dt * (adv_x + adv_z + diff)

    # Осаждение на землю
    C_new[:, 0] = 0

    # Добавляем источник
    add_source(C_new)

    C = C_new

# Визуализация
plt.imshow(C.T, origin='lower', aspect='auto')
plt.colorbar(label="Концентрация пепла")
plt.xlabel("x")
plt.ylabel("z (высота)")
plt.title("Распространение пеплового облака")
plt.savefig("kod.png")