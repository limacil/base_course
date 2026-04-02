import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 200
t = np.linspace(0, 5, frames)

# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    (x1, vx1, y1, vy1,
    x2, vx2, y2, vy2,
    x3, vx3, y3, vy3) = z
    
    dx_dt1 = vx1
    dvx_dt1 = 0
    dy_dt1 = vy1
    dvy_dt1 = - g

    if t > 2:
        dx_dt2 = vx2
        dvx_dt2 = 0
        dy_dt2 = vy2
        dvy_dt2 = - g
    else:
        dx_dt2 = 0
        dvx_dt2 = 0
        dy_dt2 = 0
        dvy_dt2 = 0

    

    dx_dt3 = vx3
    dvx_dt3 = 0.05 * np.cos(t)
    dy_dt3 = vy3
    dvy_dt3 = 0.1
    
    return (dx_dt1, dvx_dt1, dy_dt1, dvy_dt1,
            dx_dt2, dvx_dt2, dy_dt2, dvy_dt2,
            dx_dt3, dvx_dt3, dy_dt3, dvy_dt3)

# Определяем начальные значения и параметры
g = 9.8

v01 = 5
alpha1 = np.deg2rad(80)
x01 = 2.5
vx01 = v01 * np.cos(alpha1)
y01 = 2.5
vy01 = v01 * np.sin(alpha1)

v02 = 7
alpha2 = np.deg2rad(80)
x02 = 2.5
vx02 = - v02 * np.cos(alpha2)
y02 = 2.5
vy02 = v02 * np.sin(alpha2)

v03 = 0.1
alpha3 = np.deg2rad(90)
x03 = 2.5
vx03 = - v03 * np.cos(alpha3)
y03 = 2.5
vy03 = v03 * np.sin(alpha3)

z0 = (x01, vx01, y01, vy01,
      x02, vx02, y02, vy02,
      x03, vx03, y03, vy03)

sol = odeint(move_func, z0, t)

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='r')
ball2, = plt.plot([], [], 'o', color='r')
ball3, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='r')


iksi = [1.41, 1.48, 1.52, 1.67, 1.73, 1.89, 2.10, 2.24, 2.31, 2.45, 2.58, 2.63, 2.77, 2.89, 3.01, 3.15, 3.32, 3.44, 3.56, 3.60]
igriki=[0, 0.37, 0.71, 0.91, 1.17, 1.56, 1.86, 2.14, 2.7, 2.54, 2.55, 2.56, 2.69, 2.7, 2.2, 1.8, 1.45, 0.82, 0.38, 0]




plt.plot(iksi, igriki, color = 'black', ms = 8)
plt.plot([0, 6], [0, 0], color = 'black', ms = 8)
plt.plot([2.5], [2.5], color = 'red', ms = 8)   


def animate(i):
    ball1.set_data([sol[i][0]], [sol[i][2]])
    ball2.set_data([sol[i][4]], [sol[i][6]])
    ball3.set_data([sol[i][8]], [sol[i][10]])
    # ball_line.set_data(sol[:i, 0], sol[:i, 2])


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 5
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

	
ani.save('ver_2.gif', writer="pillow")