import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.01)


def diff_func(o, x):   
    y, z = o 
	
    dy_dx = y ** 2 * z
    dz_dx = z / (x + 0.01) -  y * z ** 2
    
    return dy_dx, dz_dx


y0 = 1
z0 = -3
o = y0, z0

sol = odeint(diff_func, o, x)
plt.plot(x, sol[:, 0], 'b', label='y(x)')
plt.plot(x, sol[:, 1], 'g', label='z(x)')
plt.legend()
plt.savefig('task_1.png')