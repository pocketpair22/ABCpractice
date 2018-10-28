N = int(input())
priceList = [int(input()) for i in range(N)]

priceList = list(set(priceList))
priceList.sort()
print(priceList[-2])
