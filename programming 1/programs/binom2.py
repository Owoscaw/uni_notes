

def fallingFact(alpha, k):
    prod = alpha
    for i in range(k - 1):
        prod = prod*(alpha - i)

    return prod

def fact(k):
    if k == 1:
        return 1
    else:
        return k*fact(k-1)

def binom2(alpha, k):
    return fallingFact(alpha, k)/fact(k)

print(binom2(6.5, 3))
