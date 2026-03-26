import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Сетка ---
Nx, Nz = 120, 60
dx, dz = 1.0, 1.0
dt = 0.1

# --- Параметры ---
u = 2.0
K = 0.05

# разные размеры частиц
vs_list = [0.1, 0.5, 1.0]

# отдельные поля
C = [np.zeros((Nx, Nz)) for _ in vs_list]

# вулкан
source_x = 30
source_z = Nz - 30

# сила текущего извержения
eruption_power = 0

# --- источник с "взрывами" ---
def add_source(C_fields, frame):
    global eruption_power

    # случайные импульсы (взрывы)
    if np.random.rand() < 0.1:
        eruption_power = np.random.uniform(5, 20)

    # плавное затухание
    eruption_power *= 0.9

    for i, field in enumerate(C_fields):
        vs = vs_list[i]

        # количество пепла зависит от силы
        amount = eruption_power * (1.0 / (i + 1))

        # добавляем пепел
        field[source_x-1:source_x+2, source_z] += amount

        # "выталкивание вверх" (имитация струи)
        if source_z > 2:
            field[source_x, source_z-1] += amount * 2
            field[source_x, source_z-2] += amount * 1

# --- шаг ---
def step(C, vs):
    C_new = C.copy()

    for i in range(1, Nx-1):
        for k in range(1, Nz-1):

            adv_x = -u * (C[i, k] - C[i-1, k]) / dx
            adv_z = vs * (C[i, k+1] - C[i, k]) / dz

            diff = K * (
                (C[i+1, k] - 2*C[i, k] + C[i-1, k]) / dx**2 +
                (C[i, k+1] - 2*C[i, k] + C[i, k-1]) / dz**2
            )

            C_new[i, k] = C[i, k] + dt * (adv_x + adv_z + diff)

    C_new[:, 0] = 0
    return C_new

# --- визуализация ---
fig, ax = plt.subplots()

img = ax.imshow(np.zeros((Nz, Nx)),
                origin='lower',
                aspect='auto',
                vmin=0, vmax=10)

plt.colorbar(img)

ax.set_title("Пепловое облако с импульсным извержением")
ax.set_xlabel("x")
ax.set_ylabel("z")

# --- анимация ---
def update(frame):
    global C

    for i, vs in enumerate(vs_list):
        C[i] = step(C[i], vs)

    add_source(C, frame)

    C_total = sum(C)

    img.set_array(C_total.T)
    ax.set_title(f"Шаг: {frame}")

    return [img]

ani = animation.FuncAnimation(
    fig,
    update,
    frames=250,
    interval=50,
    blit=False
)

ani.save("kod_3.gif", writer="pillow")