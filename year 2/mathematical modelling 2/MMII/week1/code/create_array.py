import numpy as np

dim1 = 2;
dim2 = 3
Mzero = np.zeros([dim1, dim2])
Mone = np.ones([dim1, dim2])
Munit = np.eye(dim2)
Mdiag = np.diag([1., 2, 3])          # 1. -> ensure this is an array of float 
Mfull = np.full([dim1, dim2], np.pi) # np.pi is 3.1415...
Mcopy = Mfull.copy()

print("Mzero=", Mzero)
print("Mone=", Mone)
print("Munit=", Munit)
print("Mdiag=", Mdiag)
print("Mfull=", Mfull)
print("Mcopy=", Mcopy)

