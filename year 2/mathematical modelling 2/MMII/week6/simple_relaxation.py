
class Matrix:    
    mat = []

    def __init__(self, *args):
        
        self.mat = [i for i in args]
        
    def printMatrix(self):
        for i in self.mat:
            for j in i:
                print(str(j) + " ", end="")
            print("")

    def __add__(self, other):
        aMat = Matrix(*self.mat)
        for i in range(len(self.mat)):
            for j in range(len(self.mat[i])):
                aMat.mat[i][j] = self.mat[i][j] + other.mat[i][j]

        return aMat

    

            

zMat = Matrix([1,0],[1,0])
iMat = Matrix([1,0],[0,1])

cMat = zMat + iMat
cMat.printMatrix()