N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
dif = abs(T - H[0] * 0.006 - A)
result = 1

for i in range(1, N):
    if abs(T - H[i] * 0.006 - A) < dif:
        dif = abs(T - H[i] * 0.006 - A)
        result = i + 1

print(result)
