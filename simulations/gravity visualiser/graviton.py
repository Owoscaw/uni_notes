import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy import optimize

M_ratio = 0.01
step = 0.005
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


fig, ax = plt.subplots()

# Defining minimisation function 
def colinear_cubic(x): 
    return x - (1 - pi_E)/np.abs(x + pi_E)**3 * (x + pi_E) - pi_E/np.abs(x - 1 + pi_E)**3 * (x - 1 + pi_E)


# Finding and plotting Lagrange points
def plot_Lagrange():

    # Finding equilateral points
    L_4 = np.array([0.5 - pi_E, np.sqrt(3)/2])
    L_5 = np.array([0.5 - pi_E, -np.sqrt(3)/2])

    # Finding colinear points
    L_1, L_2, L_3 = [[i, 0] for i in optimize.newton(colinear_cubic, [-1.0, 0, 1.0])]

    # Mark Lagrange points
    zero_potentials = np.array((L_1, L_2, L_3, L_4, L_5))
    for i in range(len(zero_potentials)):
        plt.plot(zero_potentials[i][0], zero_potentials[i][1], "H", color="slategray", markersize=5)
        plt.text(zero_potentials[i][0], zero_potentials[i][1], r'$\mathcal{}_{}$'.format("{L}", i), c="orangered", size="large")

    # Mark the celestial bodies
    plt.plot(-pi_E, 0, 'o', color="orange", markersize=10, label="Sun")
    plt.plot(pi_S, 0, 'o', color="royalblue", markersize=10, label="Earth")

    # Adding fancy stuff
    ax.add_patch(plt.Circle([0, 0], 1, alpha=0.7, color="slateGray", fill=False, linestyle=":"))
    ax.set_aspect("equal")

    return zero_potentials

# Creating sample patches
def create_mask(points, fine_step, coarse_step, size):
    # Creating high LOD grid
    x_f = np.arange(-size/2, size/2 + fine_step, fine_step) + pi_E
    y_f = np.arange(-size/2, size/2 + fine_step, fine_step)
    X, Y = np.meshgrid(x_f, y_f)

    # Filtering coarse mesh and generating fine points
    mask = np.ones(X.shape, dtype=bool)
    is_coarse_x = np.isclose(np.mod(X - pi_E, coarse_step), 0, atol=fine_step/2) | \
                  np.isclose(np.mod(X - pi_E, coarse_step), coarse_step, atol=fine_step/2)
    is_coarse_y = np.isclose(np.mod(Y, coarse_step), 0, atol=fine_step/2) | \
                  np.isclose(np.mod(Y, coarse_step), coarse_step, atol=fine_step/2)
    mask[is_coarse_x & is_coarse_y] = False

    for dx, dy in points:
        D = np.sqrt((X - dx)**2 + (Y - dy)**2)
        mask[D <= scale * 0.25] = False

    is_fine_node = ~mask & ~(is_coarse_x & is_coarse_y)
    is_coarse_node = ~mask & (is_coarse_x & is_coarse_y)
    print("fine samples: {}\ncoarse samples: {}".format(np.sum(is_fine_node), np.sum(is_coarse_node)))

    return np.ma.array(X, mask=mask), np.ma.array(Y, mask=mask)

# Defining grav potential
def find_potential(X, Y):

    V = np.zeros(X.shape)
    D_S = np.sqrt((R * X - x_S)**2 + (R * Y)**2) + step
    D_E = np.sqrt((R * X - x_E)**2 + (R * Y)**2) + step
    V -= G*(M_S/D_S + M_E/D_E)

    return V

# Plotting scalar potential
def plot_scalar_potential(fine_step=0.005, coarse_step=0.025, size=2.0*scale):

    Lpts = plot_Lagrange()
    X_m, Y_m = create_mask(Lpts, fine_step, coarse_step, size)
    X = X_m.data[0, :]
    Y = Y_m.data[:, 0]
    Z_blended = find_potential(X_m.data, Y_m.data)

    vmin = find_potential(Lpts[3][0], Lpts[3][1])
    lower, upper = vmin*1.14, vmin * 0.85

    levels = np.unique(np.sort(np.linspace(lower, upper, 40)))
    contours = plt.contour(X, Y, Z_blended, levels=levels, colors=["black", "dimgray", "darkgray"], alpha=0.7, linewidths=0.6)
    cbar = plt.colorbar(contours, label="Gravitational potential")

    return None

plot_scalar_potential()
plt.show()

