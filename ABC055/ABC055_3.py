N, M = map(int, input().split())

if N * 2 < M:
    x = M // 2 - N
    print(N + x // 2)

else:
    print(M // 2)
