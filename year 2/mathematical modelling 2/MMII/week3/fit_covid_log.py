import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 

csvData = np.genfromtxt("MMII\week3\code\covid_JuneJuly2021.csv", delimiter=",", comments="#")
data = [i[1] for i in csvData]
days = np.arange(len(data))

def func(d, A, k):
    return np.log(A) + k*d

popt, pcov = scipy.optimize.curve_fit(func, days, np.log(data), p0=[1000, 0.01])

print("A = {}, k = {}".format(popt[0],popt[1]))
print("tau = {}".format(np.log(2)/popt[1]))

plt.semilogy(days, data, "b*")
plt.semilogy(days, np.exp(func(days, *popt)), "r--", label="fit to A*exp(k*d)")
plt.show()