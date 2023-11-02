

def diagonal_matrix(dv):
    return [[dv[j] if i==j else 0.0 for i in range(len(dv))] for j in range(len(dv))]

def transpose(A):    
    return [[A[j][i] for j in range(len(A[i]))] for i in range(len(A))]

def is_zero_row(R):
    for i in R:
        if i != 0:
            return False
    return True

def is_in_RREF(A):
    has_1_in_col = [-1]*len(A[0])
    
    for i in range(len(A)-1):
        leading = True

        if is_zero_row(A[i]) and not is_zero_row(A[(i+1)%len(A)]):
            return False

        for j in range(len(A[i])):
            print(has_1_in_col)

            if A[i][j] != 0 and has_1_in_col[j] != -1:
                return False
            

            if A[i][j] == 1 and leading:
                if j <= max(has_1_in_col):
                    return False
                has_1_in_col[j] = j
                leading = False
            elif A[i][j] == 0 and leading:
                leading = True
            elif A[i][j] != 0 and leading:
                return False
            elif A[i][j] != 0 and not leading and has_1_in_col[j] != -1:
                return False
    return True
        
        
                

print(is_in_RREF([[3,1],[0,1]]))
