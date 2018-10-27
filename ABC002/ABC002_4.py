import itertools

N, M = map(int, input().split())
relationArray = []
maxFanctions = 1

for i in range(M):
    a = list(map(int, input().split()))
    relationArray.append(a)

array = range(1, N+1)
for i in range(2, N+1):
    for candidacyArray in itertools.combinations(array, i):
        if len(candidacyArray) <= maxFanctions:
            break
        
        flag = True
        for k in range(len(candidacyArray)-1):
            for l in range(k+1, len(candidacyArray)):
                if not([candidacyArray[k], candidacyArray[l]] in relationArray):
                    flag = False
                    break
            if not(flag):
                break
        if flag:
            maxFanctions = len(candidacyArray)

print(maxFanctions)
