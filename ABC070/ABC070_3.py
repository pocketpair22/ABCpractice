N = int(input())
T = [int(input()) for i in range(N)]
result = T[0]

for i in range(1, N):
    n = T[i]
    m = result
    while n % m != 0:
        m, n = n%m, m
    result = (result * T[i]) // m

print(result)
