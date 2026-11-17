import numpy as np
import pygame

_VISIBLE_WAVELENGTHS_NM = np.arange(380.0, 781.0, 5.0)
# CIE standard illuminant D65 spectral power, sampled every 5 nm.
_CIE_D65 = np.array(
    [
        49.9755, 52.3118, 54.6482, 68.7015, 82.7549, 87.1204, 91.4860,
        92.4589, 93.4318, 90.0570, 86.6823, 95.7736, 104.8650, 110.9360,
        117.0080, 117.4100, 117.8120, 116.3360, 114.8610, 115.3920,
        115.9230, 112.3670, 108.8110, 109.0820, 109.3540, 108.5780,
        107.8020, 106.2960, 104.7900, 106.2390, 107.6890, 106.0470,
        104.4050, 104.2250, 104.0460, 102.0230, 100.0000, 98.1671,
        96.3342, 96.0611, 95.7880, 92.2368, 88.6856, 89.3459, 90.0062,
        89.8026, 89.5991, 88.6489, 87.6987, 85.4936, 83.2886, 83.4939,
        83.6992, 81.8630, 80.0268, 80.1207, 80.2146, 81.2462, 82.2778,
        80.2810, 78.2842, 74.0027, 69.7213, 70.6652, 71.6091, 72.9790,
        74.3490, 67.9765, 61.6040, 65.7448, 69.8856, 72.4863, 75.0870,
        69.3398, 63.5927, 55.0054, 46.4182, 56.6118, 66.8054, 65.0941,
        63.3828,
    ],
    dtype=np.float64,
)
class Film:

    def __init__(self, size, refIndex, fluidIndex, heightScale, dt):

        if size < 2:
            raise ValueError("size must be at least 2")
        if dt <= 0:
            raise ValueError("dt must be positive")
        if refIndex <= 0 or fluidIndex <= 0:
            raise ValueError("refractive indices must be positive")
        if heightScale <= 0:
            raise ValueError("heightScale must be positive")

        self.refIndex = refIndex
        self.fluidIndex = fluidIndex
        self.heightScale = heightScale
        self.dt = dt
        self.dx = 1.0 / size

        centers = (np.arange(size, dtype=np.float32) + 0.5) * self.dx
        faces = np.arange(size + 1, dtype=np.float32) * self.dx

        self.x, self.y = np.meshgrid(centers, centers, indexing="ij")
        self.x_u, self.y_u = np.meshgrid(faces, centers, indexing="ij")
        self.x_v, self.y_v = np.meshgrid(centers, faces, indexing="ij")

        self.u = np.zeros((size + 1, size), dtype=np.float32)
        self.v = np.zeros((size, size + 1), dtype=np.float32)
        self.h = np.zeros((size, size), dtype=np.float32)



    def getPathDiff(self, theta=0.0):
        """Return the film's round-trip optical path difference in meters.

        theta is the incident angle in air, in degrees from the surface normal.
        """
        theta = self._validate_incident_angle(theta)
        sin_theta_film = np.sin(np.deg2rad(theta)) / self.fluidIndex
        if abs(sin_theta_film) >= 1:
            raise ValueError("the incident ray does not propagate in the film")

        cos_theta_film = np.sqrt(1 - sin_theta_film**2)
        return 2 * self.fluidIndex * self.h * self.heightScale * cos_theta_film

    @staticmethod
    def _validate_incident_angle(theta):
        theta = float(theta)
        if not np.isfinite(theta) or abs(theta) >= 90:
            raise ValueError("theta must be a finite angle between -90 and 90 degrees")

    @staticmethod
    def _fresnel_coefficients(
        n_incident, n_transmitted, cos_incident, cos_transmitted
    ):
        """Return the s- and p-polarized Fresnel amplitude coefficients."""
        r_s = (
            n_incident * cos_incident - n_transmitted * cos_transmitted
        ) / (
            n_incident * cos_incident + n_transmitted * cos_transmitted
        )
        r_p = (
            n_transmitted * cos_incident - n_incident * cos_transmitted
        ) / (
            n_transmitted * cos_incident + n_incident * cos_transmitted
        )
        return r_s, r_p

    @staticmethod
    def _cie1931_color_matching_functions(wavelengths_nm):
        """Approximate the CIE 1931 2-degree color-matching functions."""
        def gaussian(mu, sigma_left, sigma_right):
            sigma = np.where(wavelengths_nm < mu, sigma_left, sigma_right)
            return np.exp(-0.5 * ((wavelengths_nm - mu) * sigma) ** 2)

        x_bar = (
            1.056 * gaussian(599.8, 1 / 37.9, 1 / 31.0)
            + 0.362 * gaussian(442.0, 1 / 16.0, 1 / 26.7)
            - 0.065 * gaussian(501.1, 1 / 20.4, 1 / 26.2)
        )
        y_bar = (
            0.821 * gaussian(568.8, 1 / 46.9, 1 / 40.5)
            + 0.286 * gaussian(530.9, 1 / 16.3, 1 / 31.1)
        )
        z_bar = (
            1.217 * gaussian(437.0, 1 / 11.8, 1 / 36.0)
            + 0.681 * gaussian(459.0, 1 / 26.0, 1 / 13.8)
        )
        return np.stack((x_bar, y_bar, z_bar), axis=1)

    @staticmethod
    def _xyz_to_srgb(xyz, source_white):
        """Convert D65-white XYZ values to display-ready 8-bit sRGB."""
        bradford = np.array(
            [
                [0.8951, 0.2664, -0.1614],
                [-0.7502, 1.7135, 0.0367],
                [0.0389, -0.0685, 1.0296],
            ]
        )
        xyz_to_srgb = np.array(
            [
                [3.2406, -1.5372, -0.4986],
                [-0.9689, 1.8758, 0.0415],
                [0.0557, -0.2040, 1.0570],
            ]
        )
        d65_white = np.array([0.95047, 1.0, 1.08883])
        cone_scale = (bradford @ d65_white) / (bradford @ source_white)
        adaptation = np.linalg.inv(bradford) @ np.diag(cone_scale) @ bradford
        xyz = xyz @ adaptation.T

        linear_rgb = np.maximum(xyz @ xyz_to_srgb.T, 0)
        srgb = np.where(
            linear_rgb <= 0.0031308,
            12.92 * linear_rgb,
            1.055 * linear_rgb ** (1 / 2.4) - 0.055,
        )
        return np.rint(np.clip(srgb, 0, 1) * 255).astype(np.uint8)

    def getRGB(self, theta=0.0):
        """Return reflected D65 light as an (size, size, 3) uint8 sRGB image.
        theta is in degrees from the surface normal. The stack is air, a
        non-absorbing fluid film, and a non-absorbing substrate."""
        theta = self._validate_incident_angle(theta)
        path_diff = self.getPathDiff(theta)

        # Snell's law gives each medium's ray angle from the incident angle in air.
        sin_theta_air = np.sin(np.deg2rad(theta))
        cos_theta_air = np.cos(np.deg2rad(theta))
        cos_theta_film = np.sqrt(
            1 - (sin_theta_air / self.fluidIndex) ** 2 + 0j
        )
        cos_theta_base = np.sqrt(
            1 - (sin_theta_air / self.refIndex) ** 2 + 0j
        )

        # Fresnel amplitudes include the phase reversal at each interface.
        r01_s, r01_p = self._fresnel_coefficients(
            1.0, self.fluidIndex, cos_theta_air, cos_theta_film
        )
        r12_s, r12_p = self._fresnel_coefficients(
            self.fluidIndex, self.refIndex, cos_theta_film, cos_theta_base
        )

        wavelengths_nm = _VISIBLE_WAVELENGTHS_NM
        wavelengths_m = wavelengths_nm * 1e-9
        matching = self._cie1931_color_matching_functions(wavelengths_nm)
        wavelength_step = wavelengths_nm[1] - wavelengths_nm[0]
        integration_weights = np.ones_like(wavelengths_nm)
        integration_weights[[0, -1]] = 0.5
        weighted_illuminant = _CIE_D65 * integration_weights * wavelength_step
        y_white = np.sum(weighted_illuminant * matching[:, 1])
        source_white = np.sum(
            weighted_illuminant[:, None] * matching, axis=0
        ) / y_white

        # Sum reflected spectra in small wavelength batches to limit memory use.
        xyz = np.zeros((*self.h.shape, 3), dtype=np.float64)
        for start in range(0, wavelengths_nm.size, 8):
            stop = min(start + 8, wavelengths_nm.size)
            phase = np.exp(
                2j
                * np.pi
                * path_diff[None, :, :]
                / wavelengths_m[start:stop, None, None]
            )
            reflected_s = (r01_s + r12_s * phase) / (1 + r01_s * r12_s * phase)
            reflected_p = (r01_p + r12_p * phase) / (1 + r01_p * r12_p * phase)
            reflectance = (
                np.abs(reflected_s) ** 2 + np.abs(reflected_p) ** 2
            ) / 2

            weights = weighted_illuminant[start:stop] / y_white
            xyz += np.einsum("kij,kc,k->ijc",
                reflectance,
                matching[start:stop],
                weights,
                optimize=True,
            )

        return self._xyz_to_srgb(xyz, source_white)


    def draw_gaussian(self, x, y, sigma, amplitude=1.0):
        if sigma <= 0:
            raise ValueError("sigma must be positive")

        brush = amplitude * np.exp(
            -((self.x - x) ** 2 + (self.y - y) ** 2) / (2 * sigma**2)
        )
        self.h += brush.astype(self.h.dtype, copy=False)



    def update(self):
        h, u, v = self.h, self.u, self.v
        dx, dt = self.dx, self.dt

        h_u = np.zeros_like(u)
        h_v = np.zeros_like(v)
        grad_h_x = np.zeros_like(u)
        grad_h_y = np.zeros_like(v)
        v_at_u = np.empty_like(u)
        u_at_v = np.empty_like(v)

        # Interpolate cell-centered depth to faces to form the volume fluxes.
        h_u[1:-1, :] = 0.5 * (h[:-1, :] + h[1:, :])
        h_v[:, 1:-1] = 0.5 * (h[:, :-1] + h[:, 1:])
        # Continuity equation: dh/dt = -div(h * velocity).
        h_t = -(
            np.diff(h_u * u, axis=0) + np.diff(h_v * v, axis=1)
        ) / dx

        # Pressure-gradient terms in the momentum equations: -g * grad(h).
        # Differences between neighboring center values lie on the faces.
        grad_h_x[1:-1, :] = (h[1:, :] - h[:-1, :]) / dx
        grad_h_y[:, 1:-1] = (h[:, 1:] - h[:, :-1]) / dx

        # Interpolate the transverse velocity component onto each face grid
        # so both components of advection are available at u and v locations.
        v_at_u[1:-1, :] = 0.25 * (
            v[:-1, :-1] + v[1:, :-1] + v[:-1, 1:] + v[1:, 1:]
        )
        v_at_u[0, :] = 0.5 * (v[0, :-1] + v[0, 1:])
        v_at_u[-1, :] = 0.5 * (v[-1, :-1] + v[-1, 1:])

        u_at_v[:, 1:-1] = 0.25 * (
            u[:-1, :-1] + u[1:, :-1] + u[:-1, 1:] + u[1:, 1:]
        )
        u_at_v[:, 0] = 0.5 * (u[:-1, 0] + u[1:, 0])
        u_at_v[:, -1] = 0.5 * (u[:-1, -1] + u[1:, -1])

        # Spatial derivatives for the advective acceleration (velocity · grad).
        du_dx = np.gradient(u, dx, axis=0)
        du_dy = np.gradient(u, dx, axis=1)
        dv_dx = np.gradient(v, dx, axis=0)
        dv_dy = np.gradient(v, dx, axis=1)

        # Momentum equations without Coriolis:
        # du/dt = -g * dh/dx - u * du/dx - v * du/dy
        # dv/dt = -g * dh/dy - u * dv/dx - v * dv/dy
        # Forward-Euler step from the current state.
        u_new = u - dt * (9.81 * grad_h_x + u * du_dx + v_at_u * du_dy)
        v_new = v - dt * (9.81 * grad_h_y + u_at_v * dv_dx + v * dv_dy)

        # Forward-Euler continuity step for the cell-centered height.
        h_new = h + dt * h_t

        # Closed-wall boundary condition: normal velocity is zero at each wall.
        u_new[0, :] = 0
        u_new[-1, :] = 0
        v_new[:, 0] = 0
        v_new[:, -1] = 0

        # Advance all fields together after computing them from the old state.
        self.h, self.u, self.v = h_new, u_new, v_new



if __name__ == "__main__":
    test = Film(size=500, refIndex=1.0, fluidIndex=1.33, heightScale=1e-9, dt=1.0)
    test.update()
    print(test.h)