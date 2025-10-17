import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

data = np.genfromtxt("MMII\week3\code\data\BeetlesData.txt", delimiter=" ")
week, beetles = zip(*data)
week = np.array(week)
beetles = np.array(beetles)

# The function we want to fit
def func(t, r, k, b):
    f = k/(k*b*np.exp(-r*t)+1)
    return f 

# Fit the data X, D with the function, starting from a=0 b=0.1 
popt,pcov = scipy.optimize.curve_fit(func, week, beetles, p0=[1.0, 1000, 0.01])

print("r=", popt[0], "k=", popt[1], "b=", popt[2])

# Plot the data and the fit
plt.xlabel("X", fontsize=22)
plt.ylabel("h", fontsize=22)
plt.xticks(fontsize=20)             # Makes x labels digits larger
plt.yticks(fontsize=20)             # Makes y labels digits larger
plt.tight_layout(rect=[0, 0, 1, 1]) # Ensure the full figure is visible

plt.plot(week, beetles, "b*")                # Plot data
plt.plot(week, func(week, *popt), 'r--', label="fit to a+bx")
plt.show()



