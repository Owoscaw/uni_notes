import random as r
from matplotlib import pyplot as plt


def step(n, pause):
    plt.ion()
    plt.xlabel("time")
    plt.ylabel("step")
    plt.axhline(y=0, color="red")
    seq = [(0, 0)]

    for i in range(n):
        
        if r.random() < 0.5:
            seq.append((i, seq[i%99][1] + 1))
        else:
            seq.append((i, seq[i%99][1] - 1))

        seq = seq[-99:]

        plt.cla()
        plt.plot([i[0] for i in seq], [i[1] for i in seq], "-b")
        plt.pause(pause)

def stepXY(n, pause):
    plt.xlabel("x step")
    plt.ylabel("y step")
    seq = [(0, 0)]

    for i in range(n):
        if r.random() < 0.5:
            seq.append((seq[i][0] + 1, seq[i][1]))
        else:
            seq.append((seq[i][0], seq[i][1] + 1))

        plt.plot([i[0] for i in seq], [i[1] for i in seq], "-r")
        plt.pause(pause)
        plt.show()
    
step(1000, 0.00001)

