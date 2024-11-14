import numpy as np
import matplotlib.pyplot as plt 
import covid19

dmax = 70 # The number of days to use for the integration
cov = covid19.Covid(Rpar= 1.81, Kf=0.01, Pop=207e6)  # Set the model parameters

# Set the initial condition and the maximum length of integrationnumber of
cov.initialise(days=dmax, I0=14150) 

# Read the experimetal data from a file
cov.read_data("year 2/mathematical modelling 2/MMII/week5/code/data_BR_tot.txt", "BR")

# Plot the probability distributions
#cov.plot_probabilities()

# Integrate the equations for the specific duration
cov.iterate(dmax)

# Generate figures
cov.plot()
