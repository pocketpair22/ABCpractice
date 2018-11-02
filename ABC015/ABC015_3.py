import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]
result = True

A = [i for i in range(K)]
Alist = list(itertools.product(A, repeat=N))

for i in Alist:
    B = T[0][i[0]]
    for j in range(1, N):
        B = B ^ T[j][i[j]]
    if B == 0:
        result = False
        break

print('Nothing' if result else 'Found')

