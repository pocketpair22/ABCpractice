ABCD = input()
ABCD = list(int(ABCD[i]) for i in range(4))

for i in range(8):
    result = ABCD[0]
    for j in range(3):
        if (1<<j & i)>>j:
            result += ABCD[j+1]
        else:
            result -= ABCD[j+1]

    if result == 7:
        result = i
        break

print(ABCD[0], end='')
print('+' if 1 & result else '-', end='')
print(ABCD[1], end='')
print('+' if 10 & result else '-', end='')
print(ABCD[2], end='')
print('+' if 100 & result else '-', end='')
print(str(ABCD[3]) + '=7')
