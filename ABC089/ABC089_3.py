N = int(input())
S = [input() for _ in range(N)]
array1 = ['M', 'A', 'R', 'C', 'H']
array2 = [[] for _ in range(5)]

for i in S:
    if i[0] in array1:
        array2[array1.index(i[0])].append(i)

result = 0
for i in range(3):
    for j in range(i+1, 4):
        for k in range(j+1, 5):
            result += len(array2[i]) * len(array2[j]) * len(array2[k])

print(result)
