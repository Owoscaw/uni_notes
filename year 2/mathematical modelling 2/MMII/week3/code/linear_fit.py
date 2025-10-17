import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

X = np.array([0.0, 49, 102, 151, 197])
D = np.array([1.2, 5.1, 9.3, 13.1, 17.9])

# The function we want to fit
def func(x, a, b):
    f = a + b*x
    return f 

# Fit the data X, D with the function, starting from a=0 b=0.1 
popt,pcov = scipy.optimize.curve_fit(func, X, D, p0=[0,0.1])

print("a=", popt[0], "b=", popt[1])

# Plot the data and the fit
plt.xlabel("X", fontsize=22)
plt.ylabel("h", fontsize=22)
plt.xticks(fontsize=20)             # Makes x labels digits larger
plt.yticks(fontsize=20)             # Makes y labels digits larger
plt.tight_layout(rect=[0, 0, 1, 1]) # Ensure the full figure is visible

plt.plot(X, D, "b*")                # Plot data
plt.plot(X, func(X, *popt), 'r--', label="fit to a+bx")
plt.show()



