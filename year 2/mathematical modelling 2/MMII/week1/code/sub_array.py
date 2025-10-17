import numpy as np

print("Selecting sub-array")
M = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
print("M=", M)                   # M a 4x4 array
print("M=[0]", M[0])             # The first row of M
print("M=[:,1]", M[:,1])         # The 2nd column of M
print("M=[1:3,1:3]", M[1:3,1:3]) # The 4 elements (1,2)x(1,2) at the center of M

print("####################################")
print("Modifying the array")
# Matrix assignment
M[1] = np.array([50, 60, 70, 80])    # Modify the 2nd row
print("M=",M) 

M[:,2] = np.array([30, 7, 110, 150]) # Modify the 3rd column
print("M=",M) 

M[1:3,1:3] = np.array([[-6, -7], [-10, -11]]) # Modify the center of the array
print("M=", M) 
