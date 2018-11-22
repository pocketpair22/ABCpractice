N = int(input())
a = list(map(int, input().split()))
counter = 0

for i in range(N):
    x = a[i]
    if not x:
        continue
    while x % 2 == 0:
        x //= 2
        counter += 1

print(counter)
