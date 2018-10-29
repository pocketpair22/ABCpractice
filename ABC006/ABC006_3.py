N, M = map(int, input().split())

if M > N * 4 or M < N * 2:
    print('-1 -1 -1')

for i in range(N, -1, -1):
    if M - (i * 4) >= 0 and M - (i * 4) <= 3 * (N - i):
        if i >= M-(3*N) and i <= (M/2)-N:
            print(i-M+(3*N), M-(2*i)-(2*N), i)
            break
