N, M = map(int, input().split())
ab = []
array1 = [[] for _ in range(N+1)]
result = 0

for _ in range(M):
    a, b = map(int, input().split())
    ab.append([a, b])
    array1[a].append(b)
    array1[b].append(a)

for i in ab:
    array2 = [j[:] for j in array1]
    array2[i[0]].remove(i[1])
    array2[i[1]].remove(i[0])
    L = []
    save = []
    x = 1
    
    while True:
        if not x in L:
            L.append(x)
            save.append(x)

        if len(L) == N:
            break

        flag = True
        for j in array2[x]:
            if not j in L:
                x = j
                flag = False
                break

        if flag:
            del save[-1]
            if not save:
                result += 1
                break

            x = save[-1]

print(result)
