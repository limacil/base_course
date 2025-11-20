import numpy as np
import math

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

print("\nВведите элементы массива:")
A = np.array([[float(input(f"A[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])

print("\nВведённый массив:")
print(A)

max_in_columns = np.max(A, axis=0)

print("\nМаксимальные элементы каждого столбца:")
for j, val in enumerate(max_in_columns):
    print(f"Столбец {j+1}: {val}")
    