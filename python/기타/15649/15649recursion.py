# https://www.acmicpc.net/problem/15649
import sys
input = sys.stdin.readline


def dfs():
    if len(items) == M:
        print(' '.join(map(str, items)))
        return
    else:
        for i in range(1, N+1):
            if visited[i]:
                continue
            visited[i] = 1
            items.append(i)
            dfs()
            items.pop()
            visited[i] = 0


N, M = map(int, input().split())
sys.setrecursionlimit(10**5)
items = []
visited = [0] * (N+1)
dfs()
