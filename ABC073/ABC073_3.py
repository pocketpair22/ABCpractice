N = int(input())
maps = {}

for _ in range(N):
    A = int(input())
    if A in maps:
        maps.pop(A)
    else:
        maps[A] = 1

print(len(maps))
