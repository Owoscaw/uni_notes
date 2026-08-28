import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import matplotlib.colors as colors
import scipy

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
    L_1, L_2, L_3 = [[i, 0] for i in scipy.optimize.newton(colinear_cubic, [-1.0, 0, 1.0])]

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

    # Coarse mesh
    x_c = np.arange(-size/2, size/2 + coarse_step, coarse_step) + pi_E
    y_c = np.arange(-size/2, size/2 + coarse_step, coarse_step)
    X_c, Y_c = np.meshgrid(x_c, y_c)
    Z_c = -find_potential(X_c, Y_c) # Invert sign for LogNorm

    # Fine mesh
    x_f = np.arange(-size/2, size/2 + fine_step, fine_step) + pi_E
    y_f = np.arange(-size/2, size/2 + fine_step, fine_step)
    X_f, Y_f = np.meshgrid(x_f, y_f)

    fine_mask = np.ones(X_f.shape, dtype=bool)
    for dx, dy in Lpts:
        D = np.sqrt((X_f - dx)**2 + (Y_f - dy)**2)
        fine_mask[D <= scale * 0.25] = False

    Z_f_raw = -find_potential(X_f, Y_f)
    Z_f_masked = np.ma.array(Z_f_raw, mask=fine_mask)

    # Spacing contours
    vmin = min(Z_c.min(), Z_f_masked.compressed().min())
    vmax = max(Z_c.max(), Z_f_masked.compressed().max())
    log_norm = colors.LogNorm(vmin=vmin, vmax=vmax)

    # Render coarse potential
    plt.pcolormesh(X_c, Y_c, Z_c, norm=log_norm, cmap="viridis_r", shading='auto', alpha=0.4)
    
    # Render fine potential
    pcm = plt.pcolormesh(X_f, Y_f, Z_f_masked, norm=log_norm, cmap="viridis_r", shading='auto', alpha=0.9)
    
    cbar = plt.colorbar(pcm, label='Potential Magnitude $|V|$ (Log Scale)')

    return None

plot_scalar_potential()
plt.show()

