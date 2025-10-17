import numpy as np
import matplotlib.pyplot as plt
import random

class Spins_1d(object):
    """ A class to simulatte spin dynamics on a 1 dimentional lattice
    """
    
    def __init__(self, N, J=1.0, h=0.0, T=1):
        """
        : param N : lattice size is N 
        : param J : interaction strength
        : param h : external magnetic field
        : param T : temperature
        """
        self.N = N
        self.J = J            
        self.h = h
        self.T = T
        self.setup_lattice()
        self.setup_plotting()

    def setup_lattice(self):
        """ Setup the lattice with a configuration of all-up spins. 
        """
        self.lattice = np.ones([self.N])
            
    def setup_plotting(self):
        """ Setup a figure for interactive plotting. 
        """
        plt.close("all")
        self.live = plt.figure(figsize=(4, 1))
        plt.ion()
        plt.axis('off')
        plt.show()

    def plot_lattice(self, thermalising=False):
        """ Plot the spin configuration. 
        : param thermalising : if true display lattice in grey instead of blue
        """
        X, Y = np.meshgrid(range(self.N+1), range(2))
        cm = plt.cm.Blues
        if thermalising:
            cm = plt.cm.Greys
        # convert 1 dim array to 2 dim array
        lat = np.zeros([1,self.N])
        lat[0,:] = self.lattice              
        plt.pcolormesh(X, Y, lat, cmap=cm)
        plt.axis('off')
        plt.draw()
        plt.pause(0.01)
        #plt.cla()

    def plot_magnetisation(self, T_E_M_values):
        """
        Plot the magnetisation as a function of the temperature.
        : param T_E_M_values : list of tuples (T, E, M)
        """
        plt.close("all")
        #plt.rc('text', usetex=True)
        plt.rc('font', family='serif')
        plt.ioff()
        plt.axis('on')
        plt.xlabel('$T$')
        plt.ylabel('$M$')
        plt.title('YOUR TITLE HERE')
        # plot M as a function of T from the data in T_E_M_values

if __name__=="__main__":
      # add all your testing code here
      s = Spins_1d(5)
