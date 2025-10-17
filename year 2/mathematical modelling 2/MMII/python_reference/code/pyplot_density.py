import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

N=256
Xmin = -5
Xmax = 5
Ymin = -5
Ymax = 5
X = np.linspace(Xmin,Xmax,N) # array of X values
Y = np.linspace(Ymin,Ymax,N) # array of Y values
Z = np.empty((N,N))          # array for f(x,y) 

for i in range(0,N):
  for j in range(0,N):
    # Function to plot: f = X**2 *exp(-X*2-Y*2) 
    Z[j][i] = X[i]**2 *np.exp(-(X[i]**2+Y[j]**2)) 
 
# create the plot
plt.imshow(Z, extent = (Xmin, Xmax, Ymin, Ymax), cmap = cm.hot,aspect='auto')
plt.colorbar() # add colour bar on the right
plt.show()     # show the figure
