N, T = map(int, input().split())
t = list(map(int, input().split()))

result = T
for i in range(1, N):
    if t[i] - t[i-1] <  T:
        result += (t[i] - t[i-1])
    else:
        result += T

print(result)
