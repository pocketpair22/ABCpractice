N, K = map(int, input().split())
S = input()
ideal = sorted(S)
T = ''

for i in range(N):
    for j in range(len(ideal)):
        if S[i] == ideal[j]:
            T += ideal[j]
            del ideal[j]
            break
        number = 1
        mirror = list(ideal)
        del mirror[j]
        for k in range(i+1, N):
            if S[k] in mirror:
                mirror.remove(S[k])
            else:
                number += 1
        if K >= number:
            T += ideal[j]
            del ideal[j]
            K -= 1
            break
        
print(T)
