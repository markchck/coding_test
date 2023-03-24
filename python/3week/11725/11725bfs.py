import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [[] for i in range(N+1)]
parents = [0] * (N+1)
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    q.append(x)
    parents[x] = 1
    while q:
        v=q.popleft()
        for i in graph[v]:
            if parents[i] ==0:
                parents[i]=v
                q.append(i)
bfs(1)

for i in range(2,N+1):
    print(parents[i])