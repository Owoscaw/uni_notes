import numpy as np
import matplotlib.pyplot as plt
import random

def fill_road_randomly(road_len, density=0.1, vmax = 2):
        """ 
        Fill the road with random cars at approximate density,
        :param road_len: number of segment on the road
        :param density: target traffic density in range (0, 1)
        :param vmax: maximum speed for cars
        return : v, density
                 v : list [[p_1,s_1],[p_2,s_2], ...]
                     p_i : position of car. p_i < p_(i+1)
                     s_i : speed of car
        """
        # Creates a list of ordered positions for cars
        Ncars = int(road_len*density) # expected number of cars
        pos = sorted(list(np.random.randint(0, road_len, Ncars)))
        pos = remove_multiple(pos)
        ncars = 0
        while len(pos) != Ncars:
          # Add random extra cars
          pos += list(np.random.randint(0, road_len, Ncars-len(pos)))
          pos = remove_multiple(sorted(pos))

        # Generate random speed for each car  
        speeds = list(np.random.randint(0, vmax+1, Ncars))
        # v : list of  [p, s]             
        v = list(map(list,zip(pos, speeds)))
        
        # Compute the correct density
        density = Ncars/road_len
        
        return v, density

def make_plot(data, density, vmax, road_len, filename=''):
        """ 
        Make a space-time plot of the traffic collected in self.mat. 

        :param data : list of array configurations 
        :param density : traffic density used to generate the data
        :param vmax : maximum car speed
        :param road_len : length of the road
        :param filename: filename for the pdf figure (if not '')  
        """
        #for d in data:
        #  print("   :",d)

        mat = ps_to_array(data[0], road_len)
        for item in data[1:]:
            a = ps_to_array(item, road_len)
            mat = np.vstack([mat, a])

        np.set_printoptions(threshold=10000000)
        plt.imshow(mat >= 0, interpolation='nearest', cmap='Greys')
        plt.xlabel('position (segment)')
        plt.ylabel('time (timestep)')
        plt.title(r'$\rho$= '+str(density) + r', $v_{\rm max}$= '+ str(vmax))
        if filename!='':
            print("saving plot as", filename)
            plt.savefig(filename, bbox_inches='tight')
        plt.show()

def remove_multiple(lst):
        """ Remove multiple entries from an ordered list
            :param lst: list to prune
        """
        nlst = []
        previ= -1
        for i in lst:
             if i != previ:
                 nlst.append(i)
             previ = i
        return nlst

def ps_to_array(lst, road_len):
        pos = -np.ones(road_len)
        for ps in lst:
            pos[ps[0]] = ps[1]          
        return(pos)              
                      
