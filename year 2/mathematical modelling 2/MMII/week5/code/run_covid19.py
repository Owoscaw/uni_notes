import numpy as np
import matplotlib.pyplot as plt 
import covid19

dmax = 70 # The number of days to use for the integration
cov = covid19.Covid(Rpar= 4.55, Kf=0.01, Pop=66e6)  # Set the model parameters

# Set the initial condition and the maximum length of integrationnumber of
cov.initialise(days=dmax, I0=2.95) 

# Read the experimetal data from a file
cov.read_data("year 2/mathematical modelling 2/MMII/week5/code/data_UK_tot.txt", "UK")

# Plot the probability distributions
#cov.plot_probabilities()

# Integrate the equations for the specific duration
cov.iterate(dmax)

# Generate figures
cov.plot()
