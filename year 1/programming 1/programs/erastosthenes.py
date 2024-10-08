
def erastosthenes(n):

    trueList = [True]*n
    primes = []

    trueList[0] = False
    trueList[1] = False
    i=2
    while i**2<n:
        if trueList[i]:
            j=i
            while j*i<n:
                trueList[j*i] = False
                j += 1
        i += 1


    for k in range(n):
        if trueList[k]:
            primes.append(k)

    return primes

print(erastosthenes(10000))