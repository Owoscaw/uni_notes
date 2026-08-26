import numpy as np
import matplotlib.pyplot as plt

M_ratio = 0.01

# Astrophysical Constants
G = 6.67430e-11        # Gravitational constant (m^3 kg^-1 s^-2)
M_S = 1.989e30         # Mass of the Sun (kg)
M_E = M_ratio * M_S    # Mass of the Earth (kg)
R = 1.496e11           # Sun-Earth distance (m)

# Non-dimensionalisation
pi_E = M_E/(M_E + M_S)
pi_S = M_S/(M_E + M_S)
x_S = -pi_E * R
x_E = pi_S * R

# Mark the celestial bodies
plt.plot(x_S, 0, 'o', color="orange", markersize=20, label="Sun")
plt.plot(x_E, 0, 'o', color="royalblue", markersize=10, label="Earth")