import spacecraft as sp
import math
import numpy as np
import matplotlib.pyplot as plt

class SuperSpacecraft(sp.Spacecraft):

    def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0,m=1.0):
        super().__init__(V0, dt, t0, h, m)

        self.r_thrust = [0, 0, 0]
        self.fuel_used = 0

    def F(self,t,v):

        z = v[0]; vz = v[1]; phi = v[2]; vphi = v[3]

        self.F_theta = self.get_F_theta(v)

        if (self.r_thrust[1] < t) and (t < self.r_thrust[1] + self.r_thrust[2]):
            self.F_r = self.r_thrust[0]
        else:
            self.F_r = 0

        self.fuel_used += abs(self.F_theta)*dt

        eq1 = vz
        eq2 = -(self.G*self.M_E)/((self.r_0 + z)**2)+(self.r_0 + z)*(self.omega_0+vphi)**2 + self.F_r/self.m
        eq3 = vphi
        eq4 = (self.F_theta - 2*self.m*vz*(self.omega_0 + vphi))/(self.m*(self.r_0 + z))

        return np.array([eq1, eq2, eq3, eq4])
    
    def min_dist_to_target(self,r_thrust,tmax,dt,gdt=1):

        z0 = -1000
        v_z0 = 0
        phi0 = 0
        v_phi0 = np.sqrt((self.G*self.M_E)/((self.r_0 + z0)**3)) - self.omega_0

        self.v_phi0 = v_phi0
        self.r_thrust = r_thrust

        self.fuel_used = r_thrust[0]*r_thrust[2]

        self.reset([z0, v_z0, phi0, v_phi0], dt)
        self.iterate(tmax)

        return self.min_min()
    
    def get_F_theta(self, v):

        zero = 1e-9
        force = 2*self.m*v[1]*(self.omega_0 + v[2])

        if -zero > v[3] or v[3] > zero:
            force = -np.sign(v[3])*100

        if v[2] < -zero or v[2] > zero:
            t_decel = v[2]/100 + np.sqrt((8.15e-6)/50 - (v[2]**2)/(10000))
            force = -np.sign(v[2])*2*(8.15e-6)*self.m/(t_decel**2)

        if abs(force) >= 100:
            sign = np.sign(force)
            force = sign*100

        return force

    def get_dt(self):
        return self.dt
    
    def get_fuel_used(self):
        return self.fuel_used

    
if __name__ == '__main__':
    dt = 0.1
    gdt = 1
    s = SuperSpacecraft([0,0,0,0],dt,0,4e5,4000.) # initial condition set later
    tmax=1000

    r_thrust = [100, 0, 100]

    tmin, dmin = s.min_dist_to_target(r_thrust, tmax, dt, gdt)
    s.plot(1,3,"b-")

    print("tmin: {}, dmin: {}".format(tmin, dmin))
    print(s.get_fuel_used())

    #plt.legend(fontsize=10, loc="lower left")
    plt.plot([0],[0],'r+')
    plt.xlabel(r'$\phi$',fontsize=15)
    plt.ylabel(r'$z$',fontsize=15)
    plt.show()