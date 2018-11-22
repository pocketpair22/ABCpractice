D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
counter = 1000

for i in range(2**D):
    x = bin(i)[2:]
    x = '0' * (D-len(x)) + x
    total = 0
    newCounter=0
    for j in range(len(x)):
        if x[j] == '1':
            total += pc[j][0]*100*(j+1)+pc[j][1]
            newCounter += pc[j][0]

    if total >= G:
        counter = min(counter, newCounter)

    else:
        for j in range(len(x)-1, -1, -1):
            if x[j] == '0':
                for k in range(1, pc[j][0]):
                    total += 100*(j+1)
                    newCounter += 1
                    if total >= G:
                        counter = min(counter, newCounter)
                        break
                break

print(counter)
