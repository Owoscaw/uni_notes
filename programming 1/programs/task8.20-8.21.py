import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-4, 4, 500)
y = x
aa = x[:,None]**2 + y[None,:]**2


i = np.array([1, 2, 3, 4])
j = np.array([1, 2, 3, 4])
mm = (i[:,None] - j[None,:])**(i+j)
plt.contour(i, j, mm)
plt.gca().set_aspect('equal')
plt.show()

