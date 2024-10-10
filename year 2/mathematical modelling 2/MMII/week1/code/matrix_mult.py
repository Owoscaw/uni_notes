import numpy as np

M1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
M2 = np.diag([1,2,3])

print("M1=", M1)
print("M2=", M2)
print("M1@M2=", M1@M2)
print("M1.dot(M2)=", M1.dot(M2))
print("np.dot(M1,M2)=", np.dot(M1,M2))
