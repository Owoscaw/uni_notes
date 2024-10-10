import numpy as np
import time

dim1 = 100
dim2 = 100000
R = np.random.rand(dim1, dim2)

Ms = np.full((dim2), 1.0) # Creates a long vector initialised to 1

# SLOW
t_start = time.time()     # Time in second since 1 Jan 1970

for i in range(dim1):
  for j in range(dim2):
    Ms[j] *= R[i, j]      # M is the product of the R[i]
t_end = time.time()       # Time in second since 1 Jan 1970

print("Loop time: ", t_end-t_start)

# FAST
Mf = np.full((dim2), 1.0) # Creates a long vector initialised to 1
t_start = time.time()     # Time in second since 1 Jan 1970

for i in range(dim1):
#  TO COMPLETE
  pass                    # To remove when you complete the line above

t_end = time.time()       # Time in second since 1 Jan 1970
print("Numpy time: ", t_end-t_start)
print("(M2-M)**2=", (Mf-Ms)@(Mf-Ms))
