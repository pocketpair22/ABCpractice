H, W = map(int, input().split())
s = [input() for _ in range(H)]
case = [[1, 0], [-1, 0], [0, 1], [0, -1]]
flag = True

for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            flag = False
            for k in range(4):
                x, y = i+case[k][0], j+case[k][1]
                if x < 0 or x >= H or y < 0 or y >= W:
                    continue
                if s[x][y] == '#':
                    flag = True
                    break
            if not flag:
                break
    if not flag:
        break

print('Yes' if flag else 'No')
