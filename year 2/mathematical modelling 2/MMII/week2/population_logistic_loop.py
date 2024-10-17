from population import Population
import matplotlib.pyplot as plt

class PopulationLogistic(Population):
  """ A class to compute the time evoluation of a logistic population. """

  def __init__(self, R=0):
    """ Initialise the class instance
        : param R : population parameter
        : return : (implicitely) an instance of Population
    """
    super().__init__(R) # execute the Population class __init__ function
    
  # The only function we need to describe a population.
  def F(self):
      """ The scaled logistic population equation
      """
      return(self.R*self.N*(1-self.N))      

# Only run this when not importing the module
if __name__ == "__main__":
  R = [2.5, 2.8, 3, 3.2, 3.5, 3.8]    # The model parameters
  n_iter = 25 # The number of iteration
  for r in R:
    pop = PopulationLogistic(r)
    pop.iterate(0.1, n_iter)
    t_val = range(n_iter)
    plt.plot(t_val, pop.N_list, label="R="+str(r))

  plt.title("Logistic model") # Figure title
  plt.xlabel("t")             # Horizontal axis label
  plt.ylabel("N")             # Vertical axis label
  plt.legend()      # Displays the legends/label from the plot function "R='.."
  plt.show()