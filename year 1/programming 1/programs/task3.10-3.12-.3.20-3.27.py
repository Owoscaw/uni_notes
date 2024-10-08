
def lprod(list):
    n = 1
    for i in list:
        n = n*i
    return n

def lmean(list):
    sum = 0
    for i in list:
        sum+=i
    return sum/len(list)

def lsq(list):
    return [i**2 for i in list]

def lstdev(list):
    return (sum(lsq(list))/len(list) - (lmean(list))**2)**0.5

def lmedian(list):
    list.sort()
    if int(len(list))%2 == 0:
        medPos = int(len(list))//2 
        return lmean(list[medPos-1:medPos+1])
    else:
        return list[int(len(list))//2]

print(lmean([3,3,3,3,3]))
print(lstdev([3,1,5,2,4]))
print(lmedian([1,3,4,4]))