import random

array = []

n = random.randint(1, 12)
m = random.randint(0, (n*(n-1))/2)

print(n, m)

for i in range(m):
    flag = True
    while flag:
        x = random.randint(1, n-1)
        y = random.randint(x+1, n)
        if not([x, y] in array):
            flag = False

    print(x, y)
    array.append([x, y])
