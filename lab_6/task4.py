import matplotlib.pyplot as plt
import numpy as np

b = 0.3

phi = np.arange(0, 8*np.pi, 0.01)
r = np.exp(b * phi)

x = r * np.cos(phi)
y = r * np.sin(phi)
plt.axis('equal')
plt.plot(x, y)
plt.savefig('task4.png')