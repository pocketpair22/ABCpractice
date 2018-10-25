N = int(input())
N = N % 30
array = [1, 2, 3, 4, 5, 6]

for i in range(N):
    array[(i % 5)], array[(i % 5) + 1] = array[(i % 5) + 1], array[(i % 5)]

for i in range(6):
    print(array[i], end='')
print()
