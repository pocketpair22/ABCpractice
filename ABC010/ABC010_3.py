txa, tya, txb, tyb, T, V = map(int, input().split())
n = int(input())
girlsHouses = [list(map(int, input().split())) for i in range(n)]
result = False

for i in range(n):
    if (((txa-girlsHouses[i][0])**2+(tya-girlsHouses[i][1])**2)**0.5)+(((txb-girlsHouses[i][0])**2+(tyb-girlsHouses[i][1])**2)**0.5) <= T * V:
        result = True
        break

print('YES' if result else 'NO')
