import numpy as np
import matplotlib.pyplot as plt 
import covid19

dmax = 70 # The number of days to use for the integration
cov = covid19.Covid(Rpar= __XXX__, Kf=0.01, Pop=66e6)  # Set the model parameters

# Set the initial condition and the maximum length of integrationnumber of
cov.initialise(days=dmax, I0=1) 

# Read the experimetal data from a file
cov.read_data("data_UK_tot.txt", "UK")

# Plot the probability distributions
cov.plot_probabilities()

# Integrate the equations for the specific duration
cov.iterate(dmax)

# Generate figures
cov.plot()
