import numpy as np

def iterate(N, vJ, A, B, iMax):
    for i in range(iMax):
        N = N + vJ*(A@N - B)
    print(N)

N0 = np.array([0,0,0])
A = np.array([[-2,1,0], [1,-2,1], [0,1,-2]])
B = np.array([-1,0,0])

iterate(N0, 0.1, A, B, 30)
