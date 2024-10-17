import matplotlib.pyplot as plt
import numpy as np
import math
from population import * 

class Population_modulate(Population): #BUG1: population not capitalised, population -> Population
  """ A class to compute the time evolution of a population
      modelled by
      n(t+1) = N(t) (R + a sin(f1 t)) (1-N(t)/(K+b sin(f2 t)) 
  """

  def __init__(self, R, K, a, b, f1, f2): #BUG2: self not passed as parameter to constructor, -> self
    """ : param R : growing rate
        : param K : saturation concentration
        : param a : amplitude of growing rate modulation
        : param b : amplitude of saturation modulation
        : param f1: frequency of growing rate modulation
        : param f2: frequency of saturation modulation
    """
    # Initilise all the parameters
    self.R = R  
    self.K = K  
    self.a = a  
    self.b = b  
    self.f1 = f1  
    self.f2 = f2  #BUG3: this is meant to be f2, self.f2 = f1 -> self.f2 = f2
    self.N = 0  # current population
    self.t = 0  # to keep track of time
    
  def F(self): # BUG4: no colon after function definition
    """ Return the population at the next time. 
    """
    val = self.N*(self.R + self.a*np.sin(2*math.pi*self.f1*self.t))*\
            (1-self.N/(self.K+self.b*np.sin(2*math.pi*self.f2*self.t))) #BUG5: numpy sin function incorrectly referenced, sin -> np.sin
    # Keep track of time in the class
    self.t += 1
    return val
  

if __name__ == "__main__":
  pop = Population_modulate(R=1.25, K=1, a=0.5, b=0.2, f1=0.01, f2=0.037)
  tmax = 500
  N0 = 0.1
  # Iterate returns a list with all values of N(t)
  pop.iterate(N0, tmax) #BUG6: tmax+1 was the second parameter, making pop.N_list a dimension higher than x, tmax+1 -> tmax
  # Compute the minimum and maximum of population skipping first n0 data
  n0 = 50  #BUG7: "." included after n0 definition, making it a float which cannot be used for list slicing, 50. -> 50
  print("Nmin = {} Nmax = {}".format(min(pop.N_list[n0:]),max(pop.N_list[n0:])))
  
  x = np.linspace(0,tmax,tmax) 
  print(len(x), len(pop.N_list))
  plt.plot(x, pop.N_list, "b-") #BUG8: these four lines were indented for some reason
  plt.xlabel("x", fontsize=20)
  plt.ylabel("N", fontsize=20)
  plt.show()
