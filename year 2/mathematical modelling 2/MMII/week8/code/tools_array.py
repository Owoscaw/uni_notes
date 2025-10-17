import numpy as np
import matplotlib.pyplot as plt
import random

def fill_road_randomly(road_len, density=0.1, vmax = 2):
        """ 
        Fill the road with random cars at approximate density,
        :param road_len: number of segment on the road
        :param density: target car density
        :param vmax: maximum speed for cars
        return : v, density
                 v : an array of size road_len with
                     n >=0 : speed of the car 
                     -1 : no car
        """
        # Create an array filled with True or False, with True occuring
        # approximately at density 'ensity'.
        onoff = np.random.rand(road_len) < density

        # Create an array with random velocities for each segment,
        # taken between 0 and self.vmax.
        veloc = np.random.randint(vmax+1, size=road_len)

        # Set velocities, or -1 if there is no car in a segment.
        v = np.choose( onoff, [-1, veloc] )
        density = len(np.where( onoff )[0])/road_len
        
        return v, density

def make_plot(data, density, vmax, road_len, filename=''):
        """ 
        Make a space-time plot of the traffic collected in self.mat. 

        :param data : list of array configurations 
        :param density : target traffic density in range (0, 1)
        :param vmax : maximum car speed
        :param road_len : length of the road
        :param filename: filename for the pdf figure (if not '')  
        """
        mat = np.array(data[0])
        for item in data[1:]:
            mat = np.vstack([mat, item])

        np.set_printoptions(threshold=10000000)
        plt.imshow(mat >= 0, interpolation='nearest', cmap='Greys')
        plt.xlabel('position (segment)')
        plt.ylabel('time (timestep)')
        plt.title(r'$\rho$= '+str(density) + r', $v_{\rm max}$= '+ str(vmax))
        if filename!='':
            print("saving plot as", filename)
            plt.savefig(filename, bbox_inches='tight')
        plt.show()

