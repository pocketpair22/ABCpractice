N, K = map(int, input().split())
array = [0 for _ in range(10**5)]
for _ in range(N):
    a, b = map(int, input().split())
    array[a-1] += b

num = 0
for i in range(len(array)):
    num += array[i]
    if num >= K:
        print(i+1)
        break
