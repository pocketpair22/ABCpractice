R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [list(input()) for i in range(R)]

q = [[sy-1, sx-1]]
array = [[1, 0], [-1, 0], [0, 1], [0, -1]]

c[sy-1][sx-1] = 0
while c[gy-1][gx-1] == '.':
    for i in range(4):
        if c[q[0][0]+array[i][0]][q[0][1]+array[i][1]] == '.':
            c[q[0][0]+array[i][0]][q[0][1]+array[i][1]] = c[q[0][0]][q[0][1]]+1
            q.append([q[0][0]+array[i][0], q[0][1]+array[i][1]])
    del q[0]

print(c[gy-1][gx-1])
