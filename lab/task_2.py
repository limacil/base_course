import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)


def diff_func(o, t):   
    x, y = o 
	
    dx_dt = 3 * x - 2 * y + e ** (3 * t) / e ** t + 1
    dy_dt = x - e ** (3 * t) / e ** t + 1
    
    return dx_dt, dy_dt

e = 1
x0 = 5
y0 = -7
o = x0, y0

sol = odeint(diff_func, o, t)
plt.plot(t, sol[:, 0], 'b', label='x(t)')
plt.plot(t, sol[:, 1], 'g', label='y(t)')
plt.legend()
plt.savefig('task_2.png')