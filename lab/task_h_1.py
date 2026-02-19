import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)


def diff_func(o, t):   
    y, dy_dt = o 
	
    omega = dy_dt 
    domega_dt = - y
    
    return omega, domega_dt


y0 = 4
dy0_dt = -1
o = y0, dy0_dt

sol = odeint(diff_func, o, t)
plt.plot(t, sol[:, 0], 'b', label='x(t)')
plt.plot(t, sol[:, 1], 'g', label='y(t)')
plt.legend()
plt.savefig('task_4.png')