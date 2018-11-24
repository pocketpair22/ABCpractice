S = input()
K = int(input())
flag = True

for i in range(K):
    if S[i] != '1':
        print(S[i])
        flag = False
        break

if flag:
    print(1)
