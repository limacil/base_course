import numpy as np
import math

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

print("\nВведите элементы первого массива:")
A = np.array([[float(input(f"A[{i}][{j}] = ")) for j in range(cols)] for i in range(rows)])


def srednee_arifm(A):
    for i in range(rows * cols):
        ch = 0
        
        str = 0
        stl = 1
        
        ch += int(A[str:stl:1])
        
        #while stl <= cols:
           # str +=1
           # if stl == cols:
               # str +=1
    print(ch)


srednee_arifm(A)



