import numpy as np
import math

# Ввод размеров массива
rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

# Ввод первого массива
print("\nВведите элементы первого массива:")
A = np.array([[float(input(f"A[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])

# Ввод второго массива
print("\nВведите элементы второго массива:")
B = np.array([[float(input(f"B[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])

# Создание третьего массива — максимум поэлементно
C = np.maximum(A, B)

print("\nПервый массив A:\n", A)
print("\nВторой массив B:\n", B)
print("\nТретий массив C (максимальные элементы):\n", C)
