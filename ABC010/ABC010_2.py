n = int(input())
a = list(map(int, input().split()))
number = 0

for i in range(n):
    if a[i] % 2 == 0:
        if a[i] % 3 == 0:
            number += 3
        else:
            number += 1
    else:
        if a[i] % 3 == 2:
            number += 2

print(number)
