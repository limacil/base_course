import matplotlib.pyplot as plt
import math 


def kriv_lis(a = 1, A = 1, B = 3, b = 0.5):
    t = 1
    for i in range(5):
        x = A * math.sin(a * t + (math.pi / 2))
        y = B * math.sin(b * t)
        t += 1
    plt.plot(x, y)
    #plt.axis('equal')
    plt.savefig('task_h_1.png')


if __name__ == '__main__':
    kriv_lis()