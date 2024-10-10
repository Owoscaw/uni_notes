import numpy as np

# circular shift
print("Circular shifts on vectors")
V = np.linspace(0, 10, 6)
print("V=",V)
V2= np.roll(V,1)               # roll 1 to the right
print("roll(V,1) ->", V2)
V3= np.roll(V,-2)              # roll 2 to the left 
print("roll(V,-2) ->", V3)

V = np.linspace(0, 10, 6)
print("\nV=",V)
V2= np.roll(V, 1)              # roll 1 to the right
print("roll(V, 1) ->", V2)
V3= np.roll(V, -2)             # roll 2 to the left 
print("roll(V, -2) ->", V3)

print("\nCircular shifts on matrices")
M = np.array([[1,2,3],[3,4,5],[6,7,8]])
print("M=\n", M)
M2 =np.roll(M, 1, axis=0)      # roll 1 to the down
print("roll(M, 1, axis=0) ->\n", M2)

M3=np.roll(M,-1,axis=1)        # roll 1 to the leftt
print("roll(M, -1, axis=1) ->\n", M3)

print("\nLinear shifts")       # shift 1 to the right. fill in with zeros
V = np.linspace(0, 10, 6)
print("V=", V)
V[1:] = V[0:-1]                # we lose the original V here
V[0] = 0                       # V[0] is the old value -> set it to 0
print("shifted V=", V)
