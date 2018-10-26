N= int(input())
SE = []
for i in range(N):
    SE.append(list(map(int, input().split('-'))))
    SE[-1][0] -= SE[-1][0] % 5
    if SE[-1][1] % 5 != 0:
        SE[-1][1] += 5 - (SE[-1][1] % 5)
        if SE[-1][1] % 100 == 60:
            SE[-1][1] += 40
            
    for j in range(len(SE)-1):
        if SE[j][0] < SE[-1][0] and SE[-1][1] < SE[j][1]:
            del SE[-1]
            break
        elif SE[-1][0] < SE[j][0] and SE[j][1] < SE[-1][1]:
            SE[j] = [-1, -1]
        elif SE[j][0] <= SE[-1][0] and SE[-1][0] <= SE[j][1] and SE[j][1] <= SE[-1][1]:
            SE[-1][0] = SE[j][0]
            SE[j] = [-1, -1]
        elif SE[-1][0] <= SE[j][0] and SE[j][0] <= SE[-1][1] and SE[-1][1] <= SE[j][1]:
            SE[-1][1] = SE[j][1]
            SE[j] = [-1, -1]
    SE = [j for j in SE if j[0] != -1]
 
SE.sort()
for i in range(len(SE)):
    print(str(SE[i][0]).zfill(4)+'-'+str(SE[i][1]).zfill(4))
