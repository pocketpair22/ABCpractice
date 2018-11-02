def search(x, y):
    if x == N:
        return False if y == 0 else True
    
    for i in range(K):
        if not search(x+1, y ^ T[x][i]):
            return False

    return True

N, K = map(int, input().split())
T = [list(map(int, input().split())) for i in range(N)]

print('Nothing' if search(0, 0) else 'Found')
