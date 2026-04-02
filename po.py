import matplotlib.pyplot as plt
iksi=[0.0, 1.0, 1.3, 2.1, 2.5, 3.7, 4.8, 5.7, 6.0]
igriki=[0.0, 1.5, 2.3, 2.1, 3.1, 2.8, 3.1, 1.7, 0.2, 0.0]

plt.plot(iksi, igriki, color = 'black', marker = '.', ms = 8)
plt.axis('equal')
plt.savefig('po.jpg')
