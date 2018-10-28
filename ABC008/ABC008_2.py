from collections import Counter

N = int(input())

voteList = [input() for i in range(N)]

v = Counter(voteList)
print(v.most_common()[0][0])
