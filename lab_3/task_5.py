import numpy as np1
import task_3 as t3
a = t3.result[:5]
#print(a)
d = int(input('1ct '))
f = int(input('2ct '))
coord = a[:, d]
b = a[:, f]
a[::] = b
print(coord, b, a)