import numpy as np
import physics_constants as pc
from physics_constants import g

h = 100 #метры
a = 45 #градусы
b = 35

v_1 = g * h * np.tan(b) ** 2
v_2 = 2 * np.cos(a) ** 2 * (1 - np.tan(b) * np.tan(a))
v = np.sqrt(v_1 / v_2)

print(v)

T = 200 #К
e = 300 #Дж

N = 2 / np.sqrt(3.14) * np.sqrt(pc.h) * (pc.k_B * T) ** (3/2) * pc.ch_e ** (e / pc.k_B * T) * e ** (T / 2) 

print(N)