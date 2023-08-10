from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit = 10**9

N, M, V = map(int, input().split())
nodes = [[] for _ in range(N+1)]
for i in range(1, M+1):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s)
# print(nodes)  # [[], [2, 3, 4], [1, 4], [1], [1, 2]]

for node in nodes:
    node.sort()

visited = [0] * (N+1)
visited2 = [0] * (N+1)


def dfs(v):
    if visited[v] == 1:
        return
    else:
        visited[v] = 1
        print(v)
        for itr in nodes[v]:
            dfs(itr)


def bfs(v):
    que = deque()
    que.append(v)
    print(v)
    visited2[v] = 1
    while que:
        now = que.popleft()

        for itr in nodes[now]:
            if visited2[itr] == 0:
                visited2[itr] = 1
                que.append(itr)
                print(itr)


dfs(V)
bfs(V)
