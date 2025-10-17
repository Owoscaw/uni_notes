
def hailstoneSequence(n):
    hailSeq = [n]
    while n > 1:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
        hailSeq.append(n)

    return (hailSeq, len(hailSeq))

def findHailstoneToN(n):

    for i in range(n):
        print(hailstoneSequence(n))

def maxCollatz(n):
    hailSeq = hailstoneSequence(n)[0]
    return max(hailSeq)

print(maxCollatz(27))