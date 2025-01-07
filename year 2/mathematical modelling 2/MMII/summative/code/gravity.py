from ode_rk4 import *
import math
import copy

class Gravity(ODE_RK4):
    def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0):
        """ V0 : initial conditions for z, v_z, phi, v_phi.
        dt : integration time step
        t0 : initial time
        h : altitude of the target orbit
        """
        super().__init__(V0,dt,t0)
        self.h = h
        self.G = 6.673e-11
        self.M_E = 5.97e24
        self.R_E = 6370e3
        self.r_0 = self.R_E+h
        self.omega_0 = math.sqrt(self.G*self.M_E/self.r_0**3)
        self.F_r = 0
        self.F_theta = 0
        self.m = 1
        self.t_last = 0
        self.d_last = -1
        self.d_butlast = -1
        self.d_min = []
        self.d_max = []

    def reset(self, V0, dt, t0=0):
        """ Reset the integration parameters; see __init__ for more info."""
        super().reset(V0, dt, t0)
        self.t_last = 0
        self.d_last = -1
        self.d_butlast = -1
        self.d_min = []
        self.d_max = []

    def F(self,t,v):
        """ Equation to solve: 
            v[0] is z
            v[1] is dz/dt
            v[2] is phi
            v[3] is dphi/dt
        """

        z = v[0]; vz = v[1]; phi = v[2]; vphi = v[3]

        eq1 = vz
        eq2 = -(self.G*self.M_E)/((self.r_0 + z)**2)+(self.r_0 + z)*(self.omega_0+vphi)**2 + self.F_r/self.m
        eq3 = vphi
        eq4 = (self.F_theta - 2*self.m*vz*(self.omega_0 + vphi))/(self.m*(self.r_0 + z))
        
        return np.array([eq1, eq2, eq3, eq4])




    def dist_2_reference(self):

        return np.sqrt(self.V[0]**2 + 2*self.r_0*(self.r_0 + self.V[0])*(1 - np.cos(self.V[2])))

    def post_integration_step(self):

        d_curr = self.dist_2_reference()

        if (self.d_last < d_curr) and (self.d_last < self.d_butlast):

            self.d_min.append([self.t, d_curr])
            return True
        
        self.d_butlast = self.d_last
        self.d_last = d_curr
        self.t_last = self.t
        
        return False
        
    def min_min(self,t_after=0):

        possible_d_min = [mini for mini in self.d_min if mini[0] > t_after]
        sorted_d_mins = sorted(possible_d_min, key=lambda mini: mini[1])
        return sorted_d_mins[0]
  

