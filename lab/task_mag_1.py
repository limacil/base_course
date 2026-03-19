import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Решение задачи на динамику электрона в электромагнитном поле

# Определяем переменную величину
t = np.arange(10**(-7), 1.1*10**(-7), 10**(-11))

# Определяем функцию для системы диф. уравнений
def move_func(s, t):
    x, v_x, y, v_y, z, v_z = s

    dxdt = v_x
    dv_xdt = q / m * (Ex + v_y * Bz - By * v_z)

    dydt = v_y
    dv_ydt = q / m * (Ey + v_z * Bx - Bz * v_x)

    dzdt = v_z
    dv_zdt = q / m * (Ez + v_x * By - Bx * v_y)

    return dxdt, dv_xdt, dydt, dv_ydt, dzdt, dv_zdt

# Определяем начальные значения и параметры, входящие в систему диф. уравнений
x0 = 0
v_x0 = 10**7

y0 = 0
v_y0 = 0

z0 = 0
v_z0 = 10**7

s0 = x0, v_x0, y0, v_y0, z0, v_z0

m = 1.6 * 10**(-31)
q = 1.6 * 10**(-19)

Ex = 10**(-3)
Ey = 0
Ez = 0

Bx = 10**(-3)
By = 10**(-3)
Bz = 10**(-3)

# Решаем систему диф. уравнений
sol = odeint(move_func, s0, t)

# Строим решение в виде графика
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(sol[:, 0], sol[:, 2], sol[:, 4], label='electron trajectory')

plt.savefig('task_1.png')
