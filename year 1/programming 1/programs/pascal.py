
def pascal3(n):
    base = [1,1]
    print(base)

    for i in range(n):
        base = nextRow(base)
        print(base)

def nextRow(prevRow):
    newRow = [0]*(len(prevRow) + 1)
    for i in range(len(prevRow) + 1):
        if i == 0 or i == len(prevRow):
            newRow[i] = 1
        else:
            newRow[i] = prevRow[i-1] + prevRow[i]

    return newRow

pascal3(5)

