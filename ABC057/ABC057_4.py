from math import factorial
 
N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort()
v.reverse()
 
maxave = 0
 
for i in range(A, B+1):
    if sum(v[:i]) / i < maxave:
        continue
    
    counter1 = 1
    for j in range(i-2, -1, -1):
        if v[j] == v[i-1]:
            counter1 += 1
        else:
            break
 
    counter2 = v.count(v[i-1])
 
    now_counter = factorial(counter2) // factorial(counter2 - counter1) // factorial(counter1)
 
    if sum(v[:i]) / i == maxave:
        nummax += now_counter
    else:
        nummax = now_counter
        maxave = sum(v[:i]) / i
    
print(maxave)
print(nummax)
