N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N-1)]

for i in range(N-1):
    result = 0
    for j in range(i, N-1):
        if result <= CSF[j][1]:
            result = CSF[j][0] + CSF[j][1]
        else:
            result = CSF[j][0] + CSF[j][1] + ((-((-(result-CSF[j][1]))//CSF[j][2])) * CSF[j][2])

    print(result)

print(0)
