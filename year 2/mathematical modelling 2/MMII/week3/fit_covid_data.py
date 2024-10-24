import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize 

csvData = np.genfromtxt("MMII\week3\code\covid_JuneJuly2021.csv", delimiter=",", comments="#")
date, data = zip(*csvData)
days = np.arange(len(data))

def func(d, A, k):
    return A*np.exp(k*d)

popt, pcov = scipy.optimize.curve_fit(func, days, data, p0=[1000, 0.01])
