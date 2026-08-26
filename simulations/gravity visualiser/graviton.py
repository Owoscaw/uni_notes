import numpy as np
import matplotlib.pyplot as plt

# 1. Astrophysical Constants
G = 6.67430e-11        # Gravitational constant (m^3 kg^-1 s^-2)
M_sun = 1.989e30       # Mass of the Sun (kg)
M_earth = 5.972e24     # Mass of the Earth (kg)
D = 1.496e11           # Sun-Earth distance (1 AU in meters)

# 2. Build an Asymmetric Coordinate Grid
# We blend a coarse global grid with a dense local grid around the Earth
x_global = np.linspace(-1.1 * D, 1.1 * D, 300)
y_global = np.linspace(-1.1 * D, 1.1 * D, 300)

# Dense patch centered on the Earth to resolve its small well
x_earth_patch = np.linspace(0.95 * D, 1.05 * D, 200)
y_earth_patch = np.linspace(-0.05 * D, 0.05 * D, 200)

# Combine and sort to make a continuous, non-uniform grid
x_coords = np.unique(np.concatenate([x_global, x_earth_patch]))
y_coords = np.unique(np.concatenate([y_global, y_earth_patch]))
X, Y = np.meshgrid(x_coords, y_coords)

# 3. Calculate Potential Fields
# Distances from the center of the Sun (0, 0) and Earth (D, 0)
r_sun = np.sqrt(X**2 + Y**2)
r_earth = np.sqrt((X - D)**2 + Y**2)

# Prevent division-by-zero errors at core centers by clipping minimum radius
r_sun = np.clip(r_sun, 7e8, None)       # Sun radius boundary
r_earth = np.clip(r_earth, 6.4e6, None)  # Earth radius boundary

# Total potential scaled to MegaJoules per kilogram (MJ/kg)
V_total = -G * (M_sun / r_sun + M_earth / r_earth)
V_total_mj = V_total / 1e6

# 4. Generate the 2D Contour Plot
plt.figure(figsize=(10, 8))

# Define logarithmic or custom exponential intervals to capture deep wells and flat planes
levels = -np.geomspace(40, 2000, 30)[::-1]

# Plot filled contours for the background gradient
contour_filled = plt.contourf(X / D, Y / D, V_total_mj, levels=levels, cmap="plasma", extend="both")
cbar = plt.colorbar(contour_filled, label="Gravitational Potential (MJ / kg)")

# Overlay explicit contour lines to highlight the topology and saddle points
contours = plt.contour(X / D, Y / D, V_total_mj, levels=levels, colors="white", linewidths=0.5, alpha=0.6)

# 5. Plot Styling and Markers
plt.title("2D Gravitational Potential Contours: Sun-Earth System", fontsize=14, fontweight="bold")
plt.xlabel("X Position (AU)", fontsize=12)
plt.ylabel("Y Position (AU)", fontsize=12)

# Mark the celestial bodies
plt.plot(0, 0, 'o', color="orange", markersize=10, label="Sun")
plt.plot(1.0, 0, 'o', color="royalblue", markersize=5, label="Earth")

# Final formatting
plt.axhline(0, color="white", linestyle=":", alpha=0.3)
plt.gca().set_aspect('equal')  # Keep 1:1 aspect ratio to prevent spatial stretching
plt.legend(loc="upper left")
plt.show()