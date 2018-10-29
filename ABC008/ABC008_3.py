import math

N = int(input())
C = [int(input()) for i in range(N)]
expectedValue = 0

for i in range(N):
    divisorCounter = 0
    for j in range(N):
        if C[i] % C[j] == 0:
            divisorCounter += 1
    expectedValue += (math.factorial(divisorCounter-1) * int((divisorCounter+1)/2)) / math.factorial(divisorCounter)

print(expectedValue)
