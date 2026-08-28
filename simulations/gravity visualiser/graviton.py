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



# Defining minimisation function 
def colinear_cubic(x): 
    return x - (1 - pi_E)/np.abs(x + pi_E)**3 * (x + pi_E) - pi_E/np.abs(x - 1 + pi_E)**3 * (x - 1 + pi_E)



# Creating sample patches
def create_sample(LOD):

    # Creating low LOD meshgrid
    low_x = scale * np.linspace(-(1.0 + pi_E), 1.0 - pi_S, LOD)
    low_y = scale * np.linspace(-1.0, 1.0, LOD)
    low_X, low_Y = np.meshgrid(low_x, low_y)
    coarse_pts = np.vstack([low_X.ravel(), low_Y.ravel()]).T
    pos_coarse = np.ones(len(coarse_pts), dtype=bool)

    # Filtering coarse mesh and generating fine points
    L_points = plot_Lagrange()
    filtered_fine = []
    for dx, dy in L_points:
        D_c = np.sqrt((coarse_pts[:, 0] - dx)**2 + (coarse_pts[:, 1] - dy)**2)
        pos_coarse &= (D_c > scale * M_ratio)

        x_bb = np.arange(dx - scale * M_ratio, dx + scale * M_ratio + 5 * LOD, 5 * LOD)
        y_bb = np.arange(dy - scale * M_ratio, dy + scale * M_ratio + 5 * LOD, 5 * LOD)
        X_bb, Y_bb = np.meshgrid(x_bb, y_bb)
        pos_fine = np.vstack([X_bb.ravel(), Y_bb.ravel()]).T
        D_f = np.sqrt((pos_fine[:, 0] - dx)**2 + (pos_fine[:, 1] - dy)**2)
        square_clip = (pos_fine[:, 0] >= -scale * M_ratio) & (pos_fine[:, 0] <= scale * M_ratio) & (pos_fine[:, 1] >= -scale * M_ratio) & (pos_fine[:, 1] <= scale * M_ratio)
        filtered_fine.append(pos_fine[(D_f <= scale * M_ratio) & square_clip])

    filtered_coarse = coarse_pts[pos_coarse]

    return np.vstack([filtered_coarse] + filtered_fine)


# Finding and plotting Lagrange points
def plot_Lagrange():

    fig, ax = plt.subplots()

    # Finding equilateral points
    L_4 = scale * np.array([0.5 - pi_E, np.sqrt(3)/2])
    L_5 = scale * np.array([0.5 - pi_E, -np.sqrt(3)/2])

    # Finding colinear points
    L_1, L_2, L_3 = [[i, 0] for i in scale * scipy.optimize.newton(colinear_cubic, [-1.0, 0, 1.0])]

    # Mark Lagrange points
    zero_potentials = np.array((L_1, L_2, L_3, L_4, L_5))
    for i in range(len(zero_potentials)):
        plt.plot(zero_potentials[i][0], zero_potentials[i][1], "H", color="slategray", markersize=5)
        plt.text(zero_potentials[i][0], zero_potentials[i][1], r'$\mathcal{}_{}$'.format("{L}", i), c="orangered", size="large")

    # Mark the celestial bodies
    plt.plot(-scale * pi_E, 0, 'o', color="orange", markersize=20, label="Sun")
    plt.plot(scale * pi_S, 0, 'o', color="royalblue", markersize=10, label="Earth")

    # Adding fancy stuff
    ax.add_patch(plt.Circle([0, 0], scale, alpha=0.7, color="slateGray", fill=False, linestyle=":"))
    ax.set_aspect("equal")

    plt.legend()

    return zero_potentials


# Defining grav potential
def potential(X, Y):
    D_S = np.sqrt((X - x_S)**2 + Y**2)
    D_E = np.sqrt((X - x_E)**2 + Y**2)

    return -G*(M_S/D_S + M_E/D_E)

# Plotting scalar potential
def plot_scalar_potential(mesh):
    print(mesh)
    X = mesh[0]
    Y = mesh[1]
    plt.contour(X, Y, potential(R * X, R * Y))
    return None

temp = plot_scalar_potential(create_sample(LOD))
#temp = plot_Lagrange()
plt.show()

