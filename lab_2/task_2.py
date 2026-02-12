import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# Запись диф. уравнения в виде функции
def radio_function(n, t):
    dndt = - k * n * t
    return dndt

# Пределы изменения переменной величины
# В данной задаче переменной величиной является время
t = np.arange(0, 10, 0.01)

# Определение начальных условий и параметров
n_0 = 1000
k = 0.08

# Решение дифференциального уравнения функцией odeint
solve_Bi = odeint(radio_function, n_0, t)

# Построение решения в виде графика функции
plt.plot(t, solve_Bi[:, 0], label='деньга')
plt.xlabel('Время, года')
plt.ylabel('$')
plt.title('Количество денег')
plt.legend()

plt.savefig('task_2.png')
    