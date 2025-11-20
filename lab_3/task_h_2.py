import numpy as np
import math

n = int(input("Введите количество элементов массива (не более 10): "))
n = min(n, 10)

arr = np.array([float(input(f"arr[{i}] = ")) for i in range(n)])

print("\nИсходный массив:", arr)

value = float(input("\nВведите число для вставки: "))
pos = int(input("Введите позицию вставки (0 — начало): "))

pos = max(0, min(pos, len(arr)))

new_arr = np.insert(arr, pos, value)

print("\nНовый массив:", new_arr)
