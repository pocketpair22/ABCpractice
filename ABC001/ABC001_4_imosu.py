N= int(input())
timeTable = [0] * 289
SE = []
flag = False
for i in range(N):
    S, E = (map(int, input().split('-')))
    S = int(((int(S / 100) * 60) + (S % 100)) / 5)
    timeTable[S] += 1
    E = (int(E / 100) * 60) + (E % 100)
    if E % 5 != 0:
        E += 5 - (E % 5)
    E = int(E / 5)
    timeTable[E] -= 1

if timeTable[0] > 0:
    flag = True
    print('0000-', end='')
    
for i in range(1, 289):
    timeTable[i] += timeTable[i-1]
    if flag:
        if timeTable[i] <= 0:
            flag = False
            print(str((int((i*5)/60)*100)+(i*5)%60).zfill(4))
    else:
        if timeTable[i] > 0:
            flag = True
            print(str((int((i*5)/60)*100)+(i*5)%60).zfill(4)+'-', end='')
