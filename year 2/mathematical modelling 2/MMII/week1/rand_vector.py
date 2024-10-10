import numpy as np

dim1 = 1
dim2 = 5
M = np.random.rand(dim1, dim2)

print("M=", M)
for i in range(dim1):
  for j in range(dim2):
    print("M[",i,",",j,"]=",M[i, j])

