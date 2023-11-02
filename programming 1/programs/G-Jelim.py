

def diagonal_matrix(dv):
    return [[dv[j] if i==j else 0.0 for i in range(len(dv))] for j in range(len(dv))]

def transpose(A):    
    return [[A[j][i] for j in range(len(A[i]))] for i in range(len(A))]

print(diagonal_matrix([1,1,1]))
print(transpose([[0,0],[1,0]]))