n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
array = [0] * 1000001
minNumber = 1000000
maxNumber = 0

for i in range(n):
    array[ab[i][0]] += 1
    if ab[i][1] != 1000000:
        array[ab[i][1]+1] -= 1
    if minNumber > ab[i][0]:
        minNumber = ab[i][0]
    if maxNumber < ab[i][1]:
        maxNumber = ab[i][1]

popNumber = array[minNumber]

for i in range(minNumber+1, maxNumber+1):
    array[i] += array[i-1]
    if array[i] > popNumber:
        popNumber = array[i]
print(popNumber)
