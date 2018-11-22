N, Y = map(int, input().split())

result = None
num = 10000 * N - Y
flag = False
for i in range(N+1):
    if flag:
        break
    for j in range(N-i+1):
        if 9000 * i + 5000 * j == num:
            result = str(N-i-j) + ' ' + str(j) + ' ' + str(i)
            flag = True
            break
        elif 9000 * i + 5000 * j > num:
            break

print(result if result else '-1 -1 -1')
            
