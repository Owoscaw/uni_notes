import matplotlib.pyplot as plt
import numpy as np

class Population:
  """ A class to compute the time evolution of a population. """
  
  def __init__(self, R=0):
    """ Initialise the class instance
        : param R : population parameter
        : return : (implicitely) an instance of Population
    """
    self.R = R       # Growth rate
    self.N = 0       # Current population
    self.N_list = [] # List of all computed values
    
  def F(self):
    """ Return the population at the next time. 
    """
    return self.R*self.N
  
  def iterate(self, N0, n=0):
    """ Integrate the logistic equation n times, starting with population 
        N0 from 
    
      : param N0 :    initial population.
      : param n :     number of iteration

    self.N : contains the list of N values
    """
    
    self.N_list = []  # List of populations
    self.N = N0
    for i in range(n):
      self.N_list.append(self.N)
      self.N = self.F()

# Only run this when not importing the module.

if __name__ == "__main__":
  pop = Population(R=1.5)
  n_iter = 100                      # The number of iteration
  pop.iterate(0.1, n_iter)          # Iterate the equation F()
  t_val = range(n_iter)             # Create a list of t values
  plt.plot(t_val, pop.N_list, "r-") # Show N(t) on a graph
  plt.show()


