import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
N, M = map(int, input().split())

nodes = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
# print(nodes) [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]


def dfs(start):
    if visited[start] == 1:
        return
    else:
        visited[start] = 1
        for next in nodes[start]:
            dfs(next)


dfs_count = 0
visited = [0] * (N+1)
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(i)
        dfs_count += 1
print(dfs_count)
