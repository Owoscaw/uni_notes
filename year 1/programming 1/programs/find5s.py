
count = 0
for i in range(100000):
    for j in str(i):
        if j == "5":
            count += 1

print(count)