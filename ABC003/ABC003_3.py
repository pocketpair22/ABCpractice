N, K = input().strip().split(' ')
N, K = int(N), int(K)
R = list(map(int, input().strip().split(' ')))
C = 0

R.sort()
R = R[(N-K):]

for i in range(len(R)):
    C = (C + R[i]) / 2

print(C)
