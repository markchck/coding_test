import sys
input = sys.stdin.readline
N, M = map(int, input().split())


def dfs():
    if len(items) == M:
        print(*items)
        return
    for i in range(1, N+1):
        if visited[i] == 0 and (not items or items[-1] < i):
            items.append(i)
            visited[i] = 1
            dfs()
            items.pop()
            visited[i] = 0


items = []
visited = [0] * (N+1)
dfs()
