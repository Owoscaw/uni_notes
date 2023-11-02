

def diagonal_matrix(dv):
    return [[dv[j] if i==j else 0.0 for i in range(len(dv))] for j in range(len(dv))]

def transpose(A):    
    return [[A[j][i] for j in range(len(A[i]))] for i in range(len(A))]

def is_zero_row(R):
    for i in R:
        if i != 0:
            return False
    return True

def permute(A,r,s):
    return [A[s] if i == r else A[r] if i == s else A[i] for i in range(len(A))]

def multiply(A,r,factor):
    return [[A[i][j]*factor for j in A[i]] if i == r else A[i] for i in range(len(A))]

def add_multiply(A,r,s,factor):
    return [[A[r][j]*factor + A[i][j] for j in range(len(A[i]))] if i == s else A[i] for i in range(len(A))] 

print(add_multiply([[0,1,1],[0,0,0],[23,1,2]], 0, 1, -1))       
                

