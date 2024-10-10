import numpy as np
import numpy.linalg as la

# Transpose of a matrix
M = np.array([[1,2,3],[6,5,4],[8,7,9]],dtype=np.float64)
b = [3, 2, 1]
print("M=\n", M, "\nb=", b)

x = la.solve(M, b)
print("Mx=b -> x=\n", x)

# We test that is is correct
b2 = M@x

print("b2=M.x=\n", b2)
