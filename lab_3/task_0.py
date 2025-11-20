import numpy as np

A = np.zeros((4,6))
A = [[ 2, 3, 1, 4, 5, 6]
 [ 8, 1, 3, 2, 2, 6, 8]
 [ 1, 4, 3, 1, 0, 2, 5]
 [ 4, 5, 0, 1, 3, 2, 1]
 [ 8, 7, 9, 1, 0, 2, 3]]

slice_1 = A[3:2:1]
slice_2 = A[1,3:4,5:1]
slice_3 = A[3:6:1]
slice_4 = A[4:2:1]
slice_5 = A[3,4:3,4:1]
slice_6 = A[3:6,7:1]

print(slice_1, slice_2, slice_3, slice_4, slice_5, slice_6)