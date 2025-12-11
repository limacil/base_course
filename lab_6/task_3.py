import matplotlib.pyplot as plt
import numpy as np


def ellipce_plotter(a = 1, b = 0.5):

    x = np.arange(-2*a, 2*a, 0.1)
    y = np.arange(-2*b, 2*b, 0.1)

    # Переход к неявнозаданным координатам
    X, Y = np.meshgrid(x, y)

    fxy = X**2 / a ** 2 + Y**2 / b ** 2 # Уравнение окружности

    # Команда рисования
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')

    plt.savefig('task3.png')


if __name__ == '__main__':
    ellipce_plotter()