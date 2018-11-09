N = int(input())
a = list(map(int, input().split()))
array1 = [400, 800, 1200, 1600, 2000, 2400, 2800, 3200]
array2 = [True for _ in range(8)]
result1 = 0
plus = 0

for i in range(N):

    if a[i] >= 3200:
        plus += 1
        continue

    for j in range(8):
        if a[i] < array1[j]:
            if array2[j]:
                result1 += 1
                array2[j] = False
            break

result2 = result1 + plus

print(max(result1, 1), result2)
