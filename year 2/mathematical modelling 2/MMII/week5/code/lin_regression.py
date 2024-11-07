import numpy as np
import matplotlib.pyplot as plt 
import scipy.optimize

#Logarithm of function to fit to (B=lambda)
def linFunc(t, A, B):
    return B*t + A

def fit(data, dmin, dmax, country):

    #Selecting relevant data and taking the logarithm, excluding dmax
    relevant_data = data[dmin:dmax]
    days = np.linspace(dmin, dmax - 1, dmax - dmin)
    
    #Fitting data using a linear function
    popt, pcov = scipy.optimize.curve_fit(linFunc, days, np.log(relevant_data), p0=[1,1])
    logA, Lambda = popt

    #Plotting actual data
    plt.semilogy(days, relevant_data, "r*", label="data")

    #Plotting fitted data
    plt.semilogy(days, np.exp(linFunc(days, logA, Lambda)), "b-", label="line of best fit")

    #Decorating
    plt.axhline(0, color="black", linewidth=0.5)
    plt.xlabel("Days")
    plt.ylabel("Fatalities")
    plt.legend(loc="upper left")
    plt.show()

    #Calculating doubling time
    doubling_time = np.log(2)/Lambda

    return (country, np.exp(logA), Lambda, doubling_time)
