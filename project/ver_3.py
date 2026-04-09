import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Определяем переменную величину
frames = 300
t = np.linspace(0, 5, frames)


# Определяем функцию для системы диф. уравнений
def move_func(z, t):
    (x1, vx1, y1, vy1,
     x2, vx2, y2, vy2,
     x3, vx3, y3, vy3,
     x4, vx4, y4, vy4,
     x5, vx5, y5, vy5,
     x6, vx6, y6, vy6,
     x7, vx7, y7, vy7,
     x8, vx8, y8, vy8,
     x9, vx9, y9, vy9,
     x10, vx10, y10, vy10) = z

    dx_dt1 = vx1
    dvx_dt1 = 0
    dy_dt1 = vy1
    dvy_dt1 = - g

    if t > 1:
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
    dvx_dt3 = 0
    dy_dt3 = vy3
    dvy_dt3 = - g

    dx_dt4 = vx4
    dvx_dt4 = 0
    dy_dt4 = vy4
    dvy_dt4 = - g

    dx_dt5 = vx5
    dvx_dt5 = 0
    dy_dt5 = vy5
    dvy_dt5 = - g

    dx_dt6 = vx6
    dvx_dt6 = 0
    dy_dt6 = vy6
    dvy_dt6 = - g

    dx_dt7 = vx1
    dvx_dt7 = 0
    dy_dt7 = vy7
    dvy_dt7 = - g

    dx_dt8 = vx8
    dvx_dt8 = 0.05 * np.cos(t)
    dy_dt8 = vy8
    dvy_dt8 = 0.05

    dx_dt9 = vx9
    dvx_dt9 = 0.05 * np.cos(t)
    dy_dt9 = vy9
    dvy_dt9 = 0.12

    dx_dt10 = vx10
    dvx_dt10 = 0.05 * np.cos(t)
    dy_dt10 = vy10
    dvy_dt10 = 0.1

    return (dx_dt1, dvx_dt1, dy_dt1, dvy_dt1,
            dx_dt2, dvx_dt2, dy_dt2, dvy_dt2,
            dx_dt3, dvx_dt3, dy_dt3, dvy_dt3,
            dx_dt4, dvx_dt4, dy_dt4, dvy_dt4,
            dx_dt5, dvx_dt5, dy_dt5, dvy_dt5,
            dx_dt6, dvx_dt6, dy_dt6, dvy_dt6,
            dx_dt7, dvx_dt7, dy_dt7, dvy_dt7,
            dx_dt8, dvx_dt8, dy_dt8, dvy_dt8,
            dx_dt9, dvx_dt9, dy_dt9, dvy_dt9,
            dx_dt10, dvx_dt10, dy_dt10, dvy_dt10)


# Определяем начальные значения и параметры
g = 9.8

v01 = 3.2
alpha1 = np.deg2rad(50)
x01 = 2.6
vx01 = v01 * np.cos(alpha1)
y01 = 2.5
vy01 = v01 * np.sin(alpha1)

v02 = 4.5
alpha2 = np.deg2rad(140)
x02 = 2.65
vx02 = - v02 * np.cos(alpha2)
y02 = 2.5
vy02 = v02 * np.sin(alpha2)

v03 = 5
alpha3 = np.deg2rad(85)
x03 = 2.65
vx03 = - v03 * np.cos(alpha3)
y03 = 2.5
vy03 = v03 * np.sin(alpha3)

v04 = 7
alpha4 = np.deg2rad(110)
x04 = 2.65
vx04 = - v04 * np.cos(alpha4)
y04 = 2.5
vy04 = v04 * np.sin(alpha4)

v05 = 6
alpha5 = np.deg2rad(60)
x05 = 2.65
vx05 = - v05 * np.cos(alpha5)
y05 = 2.5
vy05 = v05 * np.sin(alpha5)

v06 = 6.5
alpha6 = np.deg2rad(100)
x06 = 2.65
vx06 = - v06 * np.cos(alpha6)
y06 = 2.5
vy06 = v06 * np.sin(alpha6)

v07 = 5.6
alpha7 = np.deg2rad(45)
x07 = 2.65
vx07 = - v07 * np.cos(alpha7)
y07 = 2.5
vy07 = v07 * np.sin(alpha7)

v08 = 0.15
alpha8 = np.deg2rad(90)
x08 = 2.6
vx08 = - v08 * np.cos(alpha8)
y08 = 2.45
vy08 = v08 * np.sin(alpha8)

v09 = 0.1
alpha9 = np.deg2rad( 90)
x09 = 2.3
vx09 = - v09 * np.cos(alpha9)
y09 = 2.5
vy09 = v09 * np.sin(alpha9)

v010 = 0.05
alpha10 = np.deg2rad(90)
x010 = 2.7
vx010 = - v010 * np.cos(alpha10)
y010 = 2.5
vy010 = v010 * np.sin(alpha10)

z0 = (x01, vx01, y01, vy01,
      x02, vx02, y02, vy02,
      x03, vx03, y03, vy03,
      x04, vx04, y04, vy04,
      x05, vx05, y05, vy05,
      x06, vx06, y06, vy06,
      x07, vx07, y07, vy07,
      x08, vx08, y08, vy08,
      x09, vx09, y09, vy09,
      x010, vx010, y010, vy010)

sol = odeint(move_func, z0, t)

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color='r')
ball2, = plt.plot([], [], 'o', color='r')
ball3, = plt.plot([], [], 'o', color='r')
ball4, = plt.plot([], [], 'o', color='r')
ball5, = plt.plot([], [], 'o', color='r')
ball6, = plt.plot([], [], 'o', color='r')
ball7, = plt.plot([], [], 'o', color='r')
ball8, = plt.plot([], [], 'o', color='b')
ball9, = plt.plot([], [], 'o', color='b')
ball10, = plt.plot([], [], 'o', color='b')
ball_line, = plt.plot([], [], '-', color='r')

iksi = [1.41, 1.48, 1.52, 1.67, 1.73, 1.89, 2.10, 2.24, 2.31, 2.45, 2.58, 2.63, 2.77, 2.89, 3.01, 3.15, 3.32, 3.44, 3.56, 3.60]
igriki =[0, 0.37, 0.71, 0.91, 1.17, 1.56, 1.86, 2.14, 2.7, 2.54, 2.55, 2.56, 2.69, 2.7, 2.2, 1.8, 1.45, 0.82, 0.38, 0]
plt.plot(iksi, igriki, color='black', ms=8)
plt.plot([0, 6], [0, 0], color='black', ms=8)
plt.plot([2.31, 2.89], [2.7, 2.7], color='red', ms=20)
plt.plot([2.31, 2.45, 2.58, 2.63, 2.77, 2.89], [2.7, 2.54, 2.55, 2.56, 2.69, 2.7], 'o', color='red', ms=10)
plt.plot([2.45, 2.58, 2.63, 2.77], [2.6, 2.6, 2.6, 2.6], 'o', color='red', ms=15)


def animate(i):
    ball1.set_data([sol[i][0]], [sol[i][2]])
    ball2.set_data([sol[i][4]], [sol[i][6]])
    ball3.set_data([sol[i][8]], [sol[i][10]])
    ball4.set_data([sol[i][12]], [sol[i][14]])
    ball5.set_data([sol[i][16]], [sol[i][18]])
    ball6.set_data([sol[i][20]], [sol[i][22]])
    ball7.set_data([sol[i][24]], [sol[i][26]])
    ball8.set_data([sol[i][28]], [sol[i][30]])
    ball9.set_data([sol[i][32]], [sol[i][24]])
    ball10.set_data([sol[i][36]], [sol[i][38]])
    # ball_line.set_data(sol[:i, 0], sol[:i, 2])


ani = FuncAnimation(fig, animate, frames=frames, interval=30)

edge = 5
ax.set_xlim(0, edge)
ax.set_ylim(0, edge)

ani.save('ver_3.gif', writer="pillow")