from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

iksi = [0, 1.0, 1.3, 2.1, 2.5, 3.7, 4.1, 4.8, 5.7, 6.0]
igriki=[0, 1.5, 1.9, 2.1, 3.1, 2.8, 3.1, 1.7, 0.2, 0]




def circle_move(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y


def animate(i):
    ball.set_data(circle_move(R=2, angle_vel=1, time=i))


if __name__ == '__main__':
    plt.plot(iksi, igriki, color = 'black', ms = 8)
    plt.plot([0, 6], [0, 0], color = 'black', ms = 8)
    plt.axis('equal')
    
    fig, ax = plt.subplots()
    ball, = plt.plot([], [], 'o', color='r', label='Ball')

    edge = 3
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, animate, frames=180, interval=30)

    ani.save('animation_2.gif') 