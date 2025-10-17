import numpy as np

# No copy during assignment
A = np.arange(1, 6, 1)
print("A=", A)
B = A
print("B=", B)
B[0] = 10
print("Set B[0] to 10")
print("A=", A)
print("B=", B)
print("Whoops!\n")

# No copy as argument of a function
def no_diagonal(C):
    n = C.shape[0] # The size of C
    for i in range (0, n):
        C[i,i] = 0
    return(C)

print("Whith a function now")
A = np.array([[1,0.5], [0.5,1]])
print("A=", A)
B = no_diagonal(A)
print("B=", B)
print("A=", A)
print("Not necessarily intended!")
