N = int(input())
nine = [9**5, 9**4, 9**3, 9**2, 9, 1]
six = [6**6, 6**5, 6**4, 6**3, 6**2, 6, 1]
counter = 100000

for i in range(N+1):
    j = N-i
    countN = 0
    for k in nine:
        if not i:
            break
        countN += i // k
        i = i % k

    countS = 0
    for k in six:
        if not j:
            break
        countS += j // k
        j = j % k

    counter = min(counter, countN+countS)

print(counter)
