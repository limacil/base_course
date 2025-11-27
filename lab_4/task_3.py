import numpy as np
from scipy.constants import g


def mechanical_energy(m, h, v):
    E = 0.5 * m * v**2 + m * g * h
    print("Полная энергия:", E, "Дж")
    return E


mechanical_energy(2.0, 10.0, 5.0)

    