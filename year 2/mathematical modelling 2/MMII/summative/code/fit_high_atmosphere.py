import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.optimize

# Reading data
data = np.genfromtxt("data/AthmDensity.csv", delimiter=",", skip_header=1)

# Converting data to np arrays
d1, d2 = zip(*data)
h = np.array(d1)
d = np.array(d2)

# Fixed variables
B = 8.82*10**7
h_0 = 1

# Fitting to logarithm of function
def log_func(x, a, l, sigma):
    return np.log(a*np.exp(-l*x) + B*((x/h_0)**(-sigma)))

popt, pcov = scipy.optimize.curve_fit(log_func, h, np.log(d))

print("a = {}\nl = {}\nsigma = {}".format(*popt))

plt.plot(h, np.exp(log_func(h, *popt)), "r-", label="curve fit")
plt.semilogy(h, d, "b*", label="data")
plt.xlabel(r"$h$")
plt.ylabel(r"$dens$")
plt.title(r"$\log\rho_\text{At}$ against $h$")
plt.legend()
plt.show()