
def polyAdd(p,q):
    if len(p) == len(q):
        return [p[i] + q[i] for i in range(len(p))]
    
    return min(p,q)

print(polyAdd([1,23,3], [2,3,1,1,3]))