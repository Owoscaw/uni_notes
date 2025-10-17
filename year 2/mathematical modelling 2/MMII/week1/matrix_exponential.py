import numpy as np

def mat_exp(M,m):
    A=np.eye(M.shape[0]) + ((1/2)**m)*M
    for i in range(m):
        A=A@A
    return A

def test_exp(d):
    M = np.random.rand(d,d)
    A = 0.1*(M-M.transpose())
    B = mat_exp(A,40)
    print(B@(B.transpose()))

test_exp(3)