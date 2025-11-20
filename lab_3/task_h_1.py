import numpy as np
import math

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

print("\nВведите элементы первого массива:")
A = np.array([[float(input(f"A[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])

print("\nВведите элементы второго массива:")
B = np.array([[float(input(f"B[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])

C = np.maximum(A, B)

print("\nПервый массив A:\n", A)
print("\nВторой массив B:\n", B)
print("\nТретий массив C (максимальные элементы):\n", C)
