import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Сетка ---
Nx, Nz = 120, 60
dx, dz = 1.0, 1.0
dt = 0.1

# --- Параметры ---

u = 2.0     # ветер
K = 0.05    # диффузия

# Разные типы частиц (мелкие → крупные)
vs_list = [0.001, 0.8, 3.0]

# Создаем отдельное поле для каждого типа частиц
C = [np.zeros((Nx, Nz)) for _ in vs_list]

# Источник (вулкан)
source_x = 30
source_z = Nz - 30

def add_source(C_fields):
    for field in C_fields:
        field[source_x-1:source_x+2, source_z] += np.random.rand() * 5

# --- Шаг моделирования ---
def step(C, vs):
    C_new = C.copy()

    for i in range(1, Nx-1):
        for k in range(1, Nz-1):

            # перенос (upwind)
            adv_x = -u * (C[i, k] - C[i-1, k]) / dx
            adv_z = vs * (C[i, k+1] - C[i, k]) / dz

            # диффузия
            diff = K * (
                (C[i+1, k] - 2*C[i, k] + C[i-1, k]) / dx**2 +
                (C[i, k+1] - 2*C[i, k] + C[i, k-1]) / dz**2
            )

            C_new[i, k] = C[i, k] + dt * (adv_x + adv_z + diff)

    # осаждение
    C_new[:, 0] = 0

    return C_new

# --- Визуализация ---
fig, ax = plt.subplots()

img = ax.imshow(np.zeros((Nz, Nx)),
                origin='lower',
                aspect='auto',
                vmin=0, vmax=5)

cbar = plt.colorbar(img)
cbar.set_label("Концентрация")

ax.set_title("Анимация пеплового облака (разные размеры частиц)")
ax.set_xlabel("x")
ax.set_ylabel("z")

# --- Анимация ---
def update(frame):
    global C

    # шаг для каждого типа частиц
    for i, vs in enumerate(vs_list):
        C[i] = step(C[i], vs)

    # источник
    add_source(C)

    # суммарная концентрация
    C_total = sum(C)

    img.set_array(C_total.T)
    ax.set_title(f"Шаг: {frame}")

    return [img]

ani = animation.FuncAnimation(
    fig,
    update,
    frames=200,
    interval=50,
    blit=False
)

ani.save("kod_2.gif", writer="pillow")