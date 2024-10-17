N = 2 # initial population
R = 3 # each couple of rabbits has 4 youngs every year on average

for t in range(51): # Compute population for 50 years
   print(t, N)
   N = R*N          # Population the next year
