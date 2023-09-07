from itertools import permutations
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

items = list(permutations(range(1, N+1), M))
items.sort(key=lambda x: x[0])
for item in items:
    print(*item)
