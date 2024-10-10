import numpy as np

MF = np.array([1, 2, 3], dtype=np.float64) # Usually what we want
MC = np.array([1, 2, 3], dtype=np.complex) # Complex array
MI = np.array([1, 2, 3], dtype=np.int64)   # Array of integers

print("MF=",MF)
print("MC=",MC)
print("MI=",MI)

ZF = np.zeros([3, 3], dtype=np.float64) # Usualily what we want
ZC = np.zeros([2, 3], dtype=np.complex) # Complex array
ZI = np.zeros([1, 4], dtype=np.int64)   # Array of integers

print("ZF=", ZF)
print("ZC=", ZC)
print("ZI=", ZI)
