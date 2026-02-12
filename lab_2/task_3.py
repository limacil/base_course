import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



def speed_function(v, t):
    dvdt = -gamma * v**2 / m + a_0
    return dvdt


t = np.arange(0, 20)
v_0 = 0
m = 0,5
gamma = 1
a_0 = 1,5

solve_Bi = odeint(speed_function, v_0, t)

plt.plot(t, solve_Bi[:, 0], label='Размножение бактерий')
plt.xlabel('Период размножения, секунды')
plt.ylabel('Количество бактерий')
plt.legend()

plt.savefig('task_3.png')
    