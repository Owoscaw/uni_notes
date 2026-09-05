import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from scipy import optimize


step = 0.005
scale = 1.5

# Astrophysical Constants
G = 6.67430e-11        # Gravitational constant (m^3 kg^-1 s^-2)
M_S = 1.989e30         # Mass of the Sun (kg)
R = 1.496e11           # Sun-Earth distance (m)
R_E = 63719990         # Earth radius (m)

def update_parameters(M_ratio):
    M_E = M_ratio * M_S    
    pi_E = M_E / (M_E + M_S)
    pi_S = M_S / (M_E + M_S)
    x_S = -pi_E * R
    x_E = pi_S * R
    omega = np.sqrt(G * (M_S + M_E) / R**3)

    return pi_E, pi_S, x_E, x_S, omega


# Defining minimisation function 
def colinear_cubic(x, pi_E): 
    return x - (1 - pi_E)/np.abs(x + pi_E)**3 * (x + pi_E) - pi_E/np.abs(x - 1 + pi_E)**3 * (x - 1 + pi_E)


# Finding and plotting Lagrange points
def find_Lagrange(pi_E):

    # Finding equilateral points
    L_4 = np.array([0.5 - pi_E, np.sqrt(3)/2])
    L_5 = np.array([0.5 - pi_E, -np.sqrt(3)/2])

    # Finding colinear points
    L_1, L_2, L_3 = [[i, 0] for i in optimize.newton(colinear_cubic, [-1.0, 0, 1.0], args=[pi_E])]

    # Mark Lagrange points
    zero_potentials = np.array((L_1, L_2, L_3, L_4, L_5))

    return zero_potentials


# Creating sample patches
def create_mask(points, fine_step, coarse_step, size, pi_E):
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


def find_potential(X, Y, x_S, x_E, pi_S, pi_E, omega):
    D_S = np.sqrt((R * X - x_S)**2 + (R * Y)**2) + step
    D_E = np.sqrt((R * X - x_E)**2 + (R * Y)**2) + step

    M_E_dynamic = (pi_E / (1 - pi_E)) * M_S        
    V_grav = -G * (M_S / D_S + M_E_dynamic / D_E)
    V_centrifugal = -0.5 * (omega**2) * ((R * X - x_S)**2 + (R * Y)**2)
    
    return (V_grav + V_centrifugal) * 10e-6


def update_plot(val, X, Y):
    global contours, lagrange_markers, lagrange_texts

    pi_E, pi_S, x_E, x_S, omega = update_parameters(val)

    Lpts = find_Lagrange(pi_E)
    Z_updated = find_potential(X, Y, x_S, x_E, pi_S, pi_E, omega)

    V_saddle = find_potential(Lpts[:, 0], Lpts[:, 1], x_S, x_E, pi_S, pi_E, omega)
    lower, upper = 1.05 * min(V_saddle), 0.95 * max(V_saddle)
    levels = np.unique(np.sort(np.linspace(lower, upper, 50)))

    if contours is not None:
        contours.remove()

    ax.cla()
    contours = ax.contour(X[0, :], Y[:, 0], Z_updated, levels=levels, cmap="plasma", alpha=0.7, linewidths=0.7)

    ax.plot(-pi_E, 0, 'o', color="orange", markersize=15, label="Sun", zorder=5)
    ax.plot(pi_S, 0, 'o', color="royalblue", markersize=10, label="Urath", zorder=5)

    updated_orbit_circle = plt.Circle([-pi_E, 0], 1, alpha=0.4, color="slategray", fill=False, linestyle=":")
    ax.add_patch(updated_orbit_circle)

    for i, pt in enumerate(Lpts):
        ax.plot(pt[0], pt[1], "H", color="black", markersize=5, zorder=4)
        ax.text(pt[0] + 0.02, pt[1] + 0.02, r'$\mathcal{}_{}$'.format(r"{L}", i+1), c="orangered", size="medium", weight="bold")

    ax.set_title('Interactive CR3BP Effective Potential', fontsize=12)
    ax.legend(loc='lower right')
    fig.canvas.draw_idle()

    

if __name__ == '__main__':

    M_ratio_init = 0.01
    pi_E, pi_S, x_E, x_S, omega = update_parameters(M_ratio_init)

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2, right=0.85)
    ax.set_aspect("equal")

    size = 2.0 * scale
    fine_step, coarse_step = 0.005, 0.05
    Lpts = find_Lagrange(pi_E)
    X_m, Y_m = create_mask(Lpts, fine_step, coarse_step, size, pi_E)
    x_1d, y_1d = X_m.data[0, :], Y_m.data[:, 0]

    Z_init = find_potential(X_m.data, Y_m.data, x_S, x_E, pi_S, pi_E, omega)
    V_saddles_init = find_potential(np.array(Lpts[:, 0]), np.array(Lpts[:, 1]), x_S, x_E, pi_S, pi_E, omega)

    lower, upper = min(V_saddles_init) * 1.05, max(V_saddles_init) * 0.95
    levels = np.unique(np.sort(np.linspace(lower, upper, 50)))

    contours = ax.contour(x_1d, y_1d, Z_init, levels=levels, cmap="plasma", alpha=0.7, linewidths=0.7)


    for i, pt in enumerate(Lpts):
        ax.plot(pt[0], pt[1], "H", color="black", markersize=5, zorder=4)
        ax.text(pt[0] + 0.02, pt[1] + 0.02, r'$\mathcal{}_{}$'.format(r"{L}", i+1), c="orangered", size="medium", weight="bold")


    plt.plot(-pi_E, 0, "o", color="orange", markersize=15, label="Sun")
    plt.plot(pi_S, 0, "o", color="royalblue", markersize=10, label="Urath")

    orbit_path = plt.Circle([-pi_E, 0], 1, alpha=0.5, color="slategray", fill=False, linestyle=":")
    ax.add_patch(orbit_path)

    ax.set_title('Interactive CR3BP Effective Potential', fontsize=12)
    ax.legend(loc='lower right')


    ax_slider = plt.axes([0.2, 0.08, 0.6, 0.03])
    M_slider = Slider(ax=ax_slider, label=r"$M_{ratio}$", valmin=0.0001, valmax=1, valinit=M_ratio_init, valfmt="%.4f", color="green")

    M_slider.on_changed(lambda val: update_plot(val, X_m.data, Y_m.data))

    plt.show()