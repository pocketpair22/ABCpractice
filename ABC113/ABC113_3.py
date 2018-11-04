import bisect

N, M = map(int, input().split())
PY = []
array = [[] for _ in range(N)]

for _ in range(M):
    P, Y = map(int, input().split())
    PY.append([P, Y])
    array[P-1].append(Y)
    
for i in range(N):
    array[i].sort()

for p, y in PY:
    n = bisect.bisect_left(array[p-1], y) + 1
    print('%06d%06d' % (p, n))
