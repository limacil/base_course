import numpy as np


def func(a, b, N):
    x = np.linspace(a, b, N)
    y = x ** 2
    print(y)
    return y


y = func(0, 10, 10)

    