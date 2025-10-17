import numpy as np
import numpy.linalg as la

# Transpose of a matrix
M = np.array([[1,2], [1,1]], dtype=np.float64)
Mt= np.transpose(M)
print("M=", M, "\nMt=", Mt)

# Inverse of a matrix
print("M=",M)
Minv = la.inv(M)
print("inv(M)=", Minv)
print("M*inv(M)=", M@Minv)

# Eigen values and eigen vectors of a matrix
lam, V = la.eig(M)
print("Eigen values", lam)
print("Right Eigen vectors array", V)

dim = M.shape[0] # The size of the square array
for i in range(dim):
    print("Eigen value:", lam[i])
    v = V[:,i]                     # Selects column i from V
    print("Eigen vector:", v)
    print("M*V-lam*V=", M@v-lam[i]*v)
