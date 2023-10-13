
def gcd(p,q):
    while p != q:
        if p > q:
            p -= q
        else:
            q -= p
    return p