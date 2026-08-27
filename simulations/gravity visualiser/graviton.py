import numpy as np
import matplotlib.pyplot as plt
import scipy

M_ratio = 0.01
LOD = 500
scale = 1.5

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

# Creating low LOD meshgrid
low_x = scale * np.linspace(-(1.0 + pi_E), 1.0 - pi_S, LOD)
low_y = scale * np.linspace(-1.0, 1.0, LOD)
low_X, low_Y = np.meshgrid(low_x, low_y)

# Finding equilateral points
L_4 = scale * np.array([0.5 - pi_E, np.sqrt(3)/2])
L_5 = scale * np.array([0.5 - pi_E, -np.sqrt(3)/2])

# Finding colinear points
def colinear_cubic(x): 
    return x - (1 - pi_E)/np.abs(x + pi_E)**3 * (x + pi_E) - pi_E/np.abs(x - 1 + pi_E)**3 * (x - 1 + pi_E)

L_1, L_2, L_3 = [[i, 0] for i in scale * scipy.optimize.newton(colinear_cubic, [-1.0, 0, 1.0])]

# Mark Lagrange points
zero_potentials = np.array((L_1, L_2, L_3, L_4, L_5))
for i in range(len(zero_potentials)):
    plt.plot(zero_potentials[i][0], zero_potentials[i][1], "o", color="red", markersize=5, label="L{}".format(i + 1))

# Mark the celestial bodies
plt.plot(-scale * pi_E, 0, 'o', color="orange", markersize=20, label="Sun")
plt.plot(scale * pi_S, 0, 'o', color="royalblue", markersize=10, label="Earth")

plt.legend()
plt.show()