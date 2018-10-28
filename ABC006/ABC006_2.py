n = int(input())

valueList = [0, 0, 1]
for i in range(3, n):
    valueList.append((valueList[-1]+valueList[-2]+valueList[-3]) % 10007)

print(valueList[n-1])
