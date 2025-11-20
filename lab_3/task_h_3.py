import numpy as np
import math

# Ввод размеров массива
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Ввод элементов массива
print("\nВведите элементы массива:")
A = np.array([[float(input(f"A[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])

# Вывод исходного массива
print("\nВведённый массив:")
print(A)

# Нахождение максимальных элементов каждого столбца
max_in_columns = np.max(A, axis=0)

# Вывод результата
print("\nМаксимальные элементы каждого столбца:")
for j, val in enumerate(max_in_columns):
    print(f"Столбец {j+1}: {val}")
    