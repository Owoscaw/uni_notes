import numpy as np

M = np.array([[1,2,3], [4,5,6]])
print("M=", M)
print("M.shape=", M.shape) # M: array of shape (2,3)

M.resize([6])
print("M=", M)
print("M.shape=", M.shape) # M now vector of shape (6)

M.resize([3,2])
print("M=", M)
print("M.shape=", M.shape) # M now array of shape (3,2)


