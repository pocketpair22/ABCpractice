N = int(input())
NG = [int(input()) for i in range(3)]
result = False

if not(N in NG):
    for i in range(100):
        if N - 3 in NG:
            if N - 2 in NG:
                if N - 1 in NG:
                    break
                else:
                    N -= 1
            else:
                N -= 2
        else:
            N -= 3
        if N <= 0:
            result = True
            break

print('YES' if result else 'NO')
