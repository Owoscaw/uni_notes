import matplotlib.pyplot as plt

t_list = []                    # List of t values
N_list = []                    # List of N values
R = 3                          # Each couple of rabbits has 4 youngs on average
N = 2                          # The initial population.

for t in range(51):            # Compute population for 50 years
  t_list.append(t)
  N_list.append(N)
  N = R*N                      # Population the next year

plt.plot(t_list, N_list, "b-") # Graph of the population
plt.ylabel('$N_{t}$')          # Add axis labels
plt.xlabel('$t$')
plt.show()                     # Diplay the figure on screen 
