import sys
input = sys.stdin.readline
N, M = map(int, input().split())
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

for n in range(N):
    targetW, targetV = items[n]
    leftItems = items[:n] + items[n+1:]
