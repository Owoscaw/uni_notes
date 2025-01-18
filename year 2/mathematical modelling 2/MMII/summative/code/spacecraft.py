import gravity as gr
import math
import numpy as np
import matplotlib.pyplot as plt

class Spacecraft(gr.Gravity):

    def __init__(self,V0=[0], dt=0.1, t0=0,h=0.0,m=1.0):
        super().__init__(V0, dt, t0, h)
        self.m = m # When F is non null the mass plays a role
        self.t_thrust = 0
        
    def F(self,t,v):
        """ Equation to solve: 
            v[0] is z
            v[1] is dz/dt
            v[2] is phi
            v[3] is dphi/dt
        """

        z = v[0]; vz = v[1]; phi = v[2]; vphi = v[3]

        # Turns off F_r, F_theta after self.t_thrust
        if t > self.t_thrust: 
            self.F_r = 0
            self.F_theta = 0

        eq1 = vz
        eq2 = -(self.G*self.M_E)/((self.r_0 + z)**2)+(self.r_0 + z)*(self.omega_0+vphi)**2 + self.F_r/self.m
        eq3 = vphi
        eq4 = (self.F_theta - 2*self.m*vz*(self.omega_0 + vphi))/(self.m*(self.r_0 + z))

        return np.array([eq1, eq2, eq3, eq4])


    def min_dist_to_target(self,Fr,Ftheta,t_thrust,tmax,dt,gdt=1):
        """ Integrate equation and determine min distance to target
            : param Fr     : radial thrust (perpendicular to orbit)
            : param Ftheta : horizontal thrust (parralet to orbit)
            : param t_thrust : duration of thrust
            : param tmax : duration of integration
            : param dt : integration time step
        """

        # Saving parameters for use in F
        self.F_r = Fr
        self.F_theta = Ftheta
        self.t_thrust = t_thrust
        
        # Initial conditions
        z0 = -1000
        v_z0 = 0
        phi0 = -2000/self.r_0
        v_phi0 = np.sqrt((self.G*self.M_E)/((self.r_0 + z0)**3)) - self.omega_0

        self.reset([z0, v_z0, phi0, v_phi0], dt)
        self.iterate(tmax)

        return self.min_min()
      

if __name__ == '__main__':
    # [[Fr, Ftheta, t_thrust, colour], ...]
    params = [[50, 100, 100, "b"], [25, 50, 200, "g"], [10, 20, 500, "r"]]

    # Iterating over each set of parameters
    for param in params:
        dt = 0.1
        gdt = 1
        s = Spacecraft([0,0,0,0],dt,0,4e5,4000.) # initial condition set later
        tmax= 4000

        # Unpacking parameters
        Fr = param[0]
        Ftheta = param[1]
        t_thrust = param[2]

        tmin,dmin = s.min_dist_to_target(Fr,Ftheta,t_thrust,tmax,dt,gdt)
        print("Fr={} Ftheta={} t_thrust={}".format(Fr,Ftheta,t_thrust))
        print("dmin={}, tmin={} Fuel={}"\
        .format(dmin,tmin,(abs(Fr)+abs(Ftheta))*t_thrust))

        # Plotting z against phi
        s.plot(1,3,'{}-'.format(param[3]))

        # Plotting origin, using this to label each trajectory too
        plt.plot([0],[0], '{}-'.format(param[3]), label=r'''$F_r=$ %s,  $F_\theta=$ %s,  $t_\text{thrust}=$ %s,
            $t_\text{min}\approx$ %s,  $d_\text{min}\approx$ %s'''%(param[0], param[1], param[2], round(tmin, 2), round(dmin, 2)))
    
    plt.legend(fontsize=10, loc="lower left")
    plt.title("Spacecraft orbits")
    plt.plot([0],[0],'r+')

    plt.xlabel(r'$\phi$',fontsize=15)
    plt.ylabel(r'$z$',fontsize=15)
    plt.show()