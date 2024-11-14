
# class Matrix:    
#     mat = []

#     def __init__(self, *args):
        
#         self.mat = [i for i in args]
        
#     def printMatrix(self):
#         for i in self.mat:
#             for j in i:
#                 print(str(j) + " ", end="")
#             print("")

#     def __add__(self, other):
#         aMat = Matrix(*self.mat)
#         for i in range(len(self.mat)):
#             for j in range(len(self.mat[i])):
#                 aMat.mat[i][j] = self.mat[i][j] + other.mat[i][j]

#         return aMat
    
#     def __mult__(self, other):

def matMult(mat, v):
    result = [0]*len(v)
    for i in range(len(v)):
        for j in range(len(v)):
            result[i] += mat[i][j]*v[j]

    return result

print(matMult([[0,0],[0,0]], [3,3]))

    
def iterate(N, vJ, A, B, iMax):


    for i in range(iMax):
        N += 1
            
