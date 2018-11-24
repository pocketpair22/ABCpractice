S = input()
T = input()
result = True

arrayS = []
arrayT = []
for i in range(len(S)):
    if S[i] in arrayS:
        if arrayT[arrayS.index(S[i])] != T[i]:
            result = False
            break
    elif T[i] in arrayT:
        result = False
        break
    else:
        arrayS.append(S[i])
        arrayT.append(T[i])

print('Yes' if result else 'No')
