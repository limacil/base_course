import numpy as np

N = int(input("Введите количество строк N: "))
M = int(input("Введите количество столбцов M: "))

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        value = np.sin((i + 1) + (j + 1))
        if value > 0:
            trigonometry_array[i, j] = value 
        else: 0

print("Результирующий массив:")
print(trigonometry_array)