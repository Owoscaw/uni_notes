import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 
import code.read_covid as rc

csvData = np.genfromtxt("MMII\week3\code\Covid19_Italy_2020.csv", delimiter=",", comments="#")
days, data = zip(*rc.rem_zeros(csvData))
days = np.array(days)
data = np.array(data)

def expFunc(d, A, k):
    return A*np.exp(k*d)

def logFunc(d, B, k):
    return np.log(B) + k*d

expPopt, expPcov = scipy.optimize.curve_fit(expFunc, days, data, p0=[1, 0.01])
logPopt, logPcov = scipy.optimize.curve_fit(logFunc, days, np.log(data), p0=[1, 0.01])

print("A, k_exp = {}".format(expPopt))
print("tau_exp = {}".format(np.log(2)/expPopt[1]))
print("B, k_log = {}".format(logPopt))
print("tau_log = {}".format(np.log(2)/logPopt[2]))

plt.semilogy(days, data, "b*")
plt.semilogy(days, expFunc(days, *expPopt), "r--")
plt.semilogy(days, logFunc(days, *logPopt), "b--")
plt.show()
