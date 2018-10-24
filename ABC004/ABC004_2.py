c = []
for i in range(4):
    array = list(map(str, input().strip().split(' ')))
    c.append(array)


for i in range(3, -1, -1):
    for j in range(3, 0, -1):
        print(c[i][j] + ' ', end='')
    print(c[i][0])
