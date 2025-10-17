import numpy as np

dim = 3

M = np.random.rand(dim,dim)
Mt = M.transpose()
S = M + Mt
eigens = np.linalg.eig(S)
print(eigens)

for i in range(len(eigens[1])):
    for j in range(len(eigens[1])):
        print("Eigenvalue {} product with {}:".format(i+1,j+1))
        print(eigens[1][i].dot(eigens[1][j]))