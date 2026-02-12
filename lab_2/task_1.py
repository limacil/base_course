import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def bact_function(n, t):

    dndt = k * n 
    n = dndt
    return dndt


t = np.arange(0, 100, 1)


n_0 = 1
k = 1 / 20

solve_Bi = odeint(bact_function, n_0, t)

plt.plot(t, solve_Bi[:, 0], label='Размножение бактерий')
plt.xlabel('Период размножения, секунды')
plt.ylabel('Количество бактерий')
plt.legend()

plt.savefig('task_1.png')
    