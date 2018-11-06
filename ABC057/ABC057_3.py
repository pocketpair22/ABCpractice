N = int(input())
array = []

for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        array.append(len(str(N//i)))

print(min(array))
