import random as r

def coinToss():
    if r.random > 0.5:
        return "H"
    else:
        return "T"

def tossCoins(n):
    heads = 0
    tossSeq = []
    for i in range(n):
        result = coinToss()
        if  result == "H":
            heads += 1

        tossSeq.append(result)

    return heads