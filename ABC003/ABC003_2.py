S = input()
T = input()
result = True

for i in range(len(S)):
    if S[i] != T[i]:
        if S[i] == '@':
            if 'atcoder@'.find(T[i]) == -1:
                result = False
                break
        elif T[i] == '@':
            if 'atcoder'.find(S[i]) == -1:
                result = False
                break
        else:
            result = False
            break

if result:
    print('You can win')
else:
    print('You will lose')
