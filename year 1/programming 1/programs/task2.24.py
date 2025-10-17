
def gcd(p,q):
    while p != q:
        if p > q:
            p -= q
        else:
            q -= p
    return p

def lcm(p,q):
    return p*q/gcd(p, q)