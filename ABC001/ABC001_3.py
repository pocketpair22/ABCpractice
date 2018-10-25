import math

Deg, Dis = input().strip().split(' ')
Deg, Dis = int(Deg), int(Dis)
DirS = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
WSlist = [0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6]
Dir = None
W = -1

windSpeed = (math.floor(((Dis / 60) * 10) + 0.5)) / 10

for i in range(1, len(DirS)):
    if ((225 * i) - 112.5) <= Deg < ((225 * i) + 112.5):
        Dir = DirS[i]
        break

if Dir == None:
    Dir = DirS[0]

for i in range(len(WSlist)):
    if windSpeed <= WSlist[i]:
        W = i
        break

if W == -1:
    W = 12

if W == 0:
    Dir = 'C'

print(Dir, W)
