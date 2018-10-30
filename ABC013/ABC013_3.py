N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())
expense = N * A

for i in range(N+1):
    j = int(((N-i)*E-H-B*i)/(D+E)+1)
    if j < 0:
        j = 0
    expense = min(A*i+C*j, expense)

print(expense)
