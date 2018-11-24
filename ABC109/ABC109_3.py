def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N, X = map(int, input().split())
x = list(map(int, input().split()))
x.append(X)
x.sort()
array = []
for i in range(N):
    array.append(x[i+1]-x[i])

if len(array) > 1:
    result = gcd(array[0], array[1])
    for i in range(2, len(array)):
        result = gcd(result, array[i])
else:
    result = array[0]
    
print(result)
