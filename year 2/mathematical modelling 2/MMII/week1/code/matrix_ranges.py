import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 1, 0.1)           # A simple example
print("np.arange(0, 1, 0.1) ->",x) # 1 is not included


x = np.linspace(0, 1, 11)          # A simple example. 1 is included
print("linspace(0, 1, 11) ->",x)

x = np.linspace(0, 2*np.pi,200)    # 200 points for the figure
y = np.sin(x+0.1*x*2)/(1+x**3)     # A function

plt.plot(x,y, "b-")
plt.xlabel("x")
plt.ylabel("y")
plt.title("F(x)= sin(x+0.1*x**2)/(1+x**3)")
plt.show()
          
