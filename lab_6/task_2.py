import matplotlib.pyplot as plt
import numpy as np

n1 = -5
n2 = 5
N = 10


def hyperbola_plotter(k = 1):
  
    x = np.linspace(-10, 10, 100)
    y =  k / x
        
    plt.plot(x, y, label='my hyperbola')
    plt.xlabel('coord - x')
    plt.ylabel('coord - y')
    plt.title('hyperbola_plotter')
    plt.legend()
    plt.savefig('task2.png')
    


if __name__ == '__main__':
    
    hyperbola_plotter()