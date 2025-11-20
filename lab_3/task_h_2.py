import numpy as np
import math

# Ввод длины массива
n = int(input("Введите количество элементов массива (не более 10): "))
n = min(n, 10)

# Ввод массива
arr = np.array([float(input(f"arr[{i}] = ")) for i in range(n)])

print("\nИсходный массив:", arr)

# Ввод числа и позиции
value = float(input("\nВведите число для вставки: "))
pos = int(input("Введите позицию вставки (0 — начало): "))

# Проверка границ
pos = max(0, min(pos, len(arr)))

# Вставка элемента
new_arr = np.insert(arr, pos, value)

print("\nНовый массив:", new_arr)
