sum = 0
for i in range(5):
    sum += i + 1

def sumints(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    return sum

print(sum)

