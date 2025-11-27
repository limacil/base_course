import numpy as np


def srednee_arifm(a):
    mean_arfm = 0
    i = 0
    ch = 1
    for i in range(len(test)):
        ch *= test[i]
        i += 1
    mean_arfm = ch / len(test)
    print(mean_arfm)


test = np.array([3, 8, 9, 34, 8])
srednee_arifm(test)
    