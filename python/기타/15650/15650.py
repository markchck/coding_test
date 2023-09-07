from itertools import permutations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
items = list(permutations(range(1, N+1), M))

answer = []
for item in items:
    first = item[0]
    temp = [first]
    for i in range(1, len(item)):
        if first < item[i]:
            temp.append(item[i])
            first = item[i]
    if len(temp) == M:
        answer.append(temp)
for ans in answer:
    print(*ans)
