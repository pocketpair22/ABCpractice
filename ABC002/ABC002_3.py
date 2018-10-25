pointList = []
array = list(map(int, input().strip().split(' ')))
for i in range(3):
    pointList.append([array[i*2], array[i*2+1]])

adjustList = []
for i in range(1,3):
    array = []
    for j in range(2):
        array.append(pointList[i][j] - pointList[0][j])
    adjustList.append(array)
    
print(abs((adjustList[0][0] * adjustList[1][1]) - (adjustList[0][1] * adjustList[1][0])) / 2)
