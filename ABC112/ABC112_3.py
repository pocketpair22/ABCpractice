N = int(input())
xyh = []
for _ in range(N):
    x, y, h = map(int, input().split())
    if h != 0:
        xyh.append([x, y, h])

if len(xyh) == 1:
    Cx, Cy, H = xyh[0][0], xyh[0][1], xyh[0][2]

elif len(xyh) == 2:
    if xyh[0][2] > xyh[1][2]:
        Cx, Cy, H = xyh[0][0], xyh[0][1], xyh[0][2]
    else:
        Cx, Cy, H = xyh[1][0], xyh[1][1], xyh[1][2]

else:
    flag = False
    for i in range(101):
        for j in range(101):
            sampleH = xyh[0][2] + abs(i-xyh[0][0]) + abs(j-xyh[0][1])
            for k in range(1, len(xyh)):
                flag = True
                if xyh[k][2] + abs(i-xyh[k][0]) + abs(j-xyh[k][1]) != sampleH:
                    flag = False
                    break
            if flag:
                Cx, Cy, H = i, j, sampleH
                break
        if flag:
            break

print(Cx, Cy, H)
