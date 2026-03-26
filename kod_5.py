import matplotlib.pyplot as plt
import numpy as np


def circle_plotter():
    
    alpha = 45
    v_0 = 5

    
    x = np.arange(0, 5, 1)
    y = x * np.tan(alpha) - (9.8 * x ** 2) / (2 * v_0 ** 2 * np.cos(alpha) ** 2)

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('kod_5.png')


if __name__ == '__main__':
    circle_plotter()