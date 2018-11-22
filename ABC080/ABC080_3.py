N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]
result = -(10 ** 7) * 100

for i in range(1, 1024):
    array = []
    num = i
    for _ in range(10):
        array.append(num%2)
        num //= 2

    point = 0
    for j in range(N):
        counter = 0
        for k in range(10):
            if array[k] == 1 and F[j][k] == 1:
                counter += 1

        point += P[j][counter]

    result = max(result, point)

print(result)
