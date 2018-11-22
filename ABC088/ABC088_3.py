c = [list(map(int, input().split())) for _ in range(3)]

array = []
for i in c:
    array.append([i[0]-i[1], i[0]-i[2]])

print('Yes' if array[0] == array[1] and array[0] == array[2] else 'No')
