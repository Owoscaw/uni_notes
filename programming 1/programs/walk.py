import random as r

def plotWalk(n):
    seq = [0]

    for i in range(n-1):
        if r.random() > 0.5:
            seq.append(seq[i-1] + 1)
        else:
            seq.append(seq[i-1] - 1)

    return seq

def timeTo0():
    length = 0
    step = 0

    while step != 0 or length == 0:
        if r.random() > 0.5:
            step += 1
        else:
            step -= 1
        length += 1

    return length


print(timeTo0())