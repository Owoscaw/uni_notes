import spacecraft as sp
import math
import numpy as np
import matplotlib.pyplot as plt

class SuperSpacecraft(sp.Spacecraft):

    def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0,m=1.0):
        super().__init__(V0, dt, t0, h, m)

        self.r_thrust = [0, 0, 0, 0]
        self.th_thrust = [0, 0, 0, 0]

    def F(self,t,v):

        z = v[0]; vz = v[1]; phi = v[2]; vphi = v[3]

        if (self.r_thrust[1] < t) and (t < self.r_thrust[1] + self.r_thrust[3]):
            self.F_r = self.r_thrust[0]
        elif (self.r_thrust[2] < t) and (t < self.r_thrust[2] + self.r_thrust[3]):
            self.F_r = -self.r_thrust[0]
        else:
            self.F_r = 0



        eq1 = vz
        eq2 = -(self.G*self.M_E)/((self.r_0 + z)**2)+(self.r_0 + z)*(self.omega_0+vphi)**2 + self.F_r/self.m
        eq3 = vphi
        eq4 = (self.F_theta - 2*self.m*vz*(self.omega_0 + vphi))/(self.m*(self.r_0 + z))

        return np.array([eq1, eq2, eq3, eq4])
    
    def min_dist_to_target(self,r_thrust,th_thrust,tmax,dt,gdt=1):

        self.r_thrust = r_thrust
        self.th_thrust = th_thrust

        z0 = -1000
        v_z0 = 0
        phi0 = -2000/self.r_0
        v_phi0 = np.sqrt((self.G*self.M_E)/((self.r_0 + z0)**3)) - self.omega_0
        self.reset([z0, v_z0, phi0, v_phi0], dt)
        self.iterate(tmax)

        return self.min_min()
        
    

    
if __name__ == '__main__':
    dt = 0.1
    gdt = 1
    s = SuperSpacecraft([0,0,0,0],dt,0,4e5,4000.) # initial condition set later
    tmax=4000

    #[F_r/F_theta, t_accel, t_decel, duration] 
    r_thrust = [1000, 0, 400, 50]
    th_thrust = [0, 0, 0, 0]

    tmin,dmin = s.min_dist_to_target(r_thrust, th_thrust,tmax,dt,gdt)
    s.plot(1,3,'b-')
    print("tmin: {}, dmin: {}".format(tmin, dmin))

    #plt.legend(fontsize=10, loc="lower left")
    plt.plot([0],[0],'r+')
    plt.xlabel(r'$\phi$',fontsize=15)
    plt.ylabel(r'$z$',fontsize=15)
    plt.show()