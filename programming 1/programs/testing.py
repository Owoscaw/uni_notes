
def tayarctan(m):
    return [(-1)**((i-1)/2)*(1/i) if i%2 == 1 else 0.0 for i in range(m)]

def parsumarctan(n, x):
    arctancoef = tayarctan(n)
    arctaneval = [arctancoef[i]*x**i for i in range(n)]
    return [sum(arctaneval[:i+1]) for i in range(n)]

print(parsumarctan(5,0.5))