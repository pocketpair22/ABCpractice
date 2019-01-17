def is_prime(q):
    routeq = int(q ** 0.5) + 1
    for i in range(2, routeq):
        if q % i == 0:
            return False

    return True

N = int(input())

counter = 1
num = 11
print(str(num), end = '')

while counter < N:
    num += 10
    if is_prime(num):
        print(' ' + str(num), end = '')
        counter += 1

print()
