import numpy as np
import matplotlib.pyplot as plt

# сетка
x = np.linspace(1, 100, 200)
z = np.linspace(0, 50, 100)
X, Z = np.meshgrid(x, z)

# параметры
q = 10      # мощность источника
u = 2       # ветер
h = 20      # высота
sigma_z = 0.1 * X
sigma_y = 0.1 * X

# чтобы не делить на 0
sigma_z[sigma_z == 0] = 1
sigma_y[sigma_y == 0] = 1

# формула
C = (q / (2 * np.pi * sigma_y * sigma_z * u)) * (
    np.exp(-(Z - h)**2 / sigma_z**2) +
    np.exp(-(Z + h)**2 / sigma_z**2)
)

# график
plt.imshow(C, origin='lower', aspect='auto')
plt.colorbar(label="Концентрация")
plt.title("Гауссов шлейф")
plt.xlabel("x")
plt.ylabel("z")
plt.savefig("kod_4.png")




import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определяем переменную величину
t = np.arange(0, 10, 0.01)


# Определяем функцию для системы диф. уравнений
def diff_func(z, t): # z - изменяемая величина для системы  
    q, u, h, sigma_z, sigma_y = z # Указание изменяемых функций, через z
	
    C = (q / (2 * np.pi * sigma_y * sigma_z * u)) * (
    np.exp(-(Z - h)**2 / sigma_z**2) +
    np.exp(-(Z + h)**2 / sigma_z**2)
    
    return C


# Определяем начальные значения и параметры,
# входящие в систему диф. уравнений

q = 10      # мощность источника
u = 2       # ветер
h = 20      # высота
sigma_z = 0.1 * X
sigma_y = 0.1 * X

# Начальное значение изменяемой величины системы
z0 = q, u, h, sigma_z, sigma_y
 


# Решаем систему диф. уравнений
sol = odeint(diff_func, z0, t)

# Строим решение в виде графика
plt.plot(t, sol[:, 0], 'b', label='theta(t)')

plt.legend()
plt.savefig("kod_4.png")