# 실내에서 실내만 가도 되네?
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
items = list(map(int, input().strip()))
nodes = [[] for _ in range(N+1)]
que = deque()
for _ in range(N-1):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)
count = 0
for i in range(1, N+1):
    visit = [0] * (N+1)
    # 시작노드가 실외이면 continue
    if items[i-1] == 0:
        continue
    que.append(i)
    while que:
        now = que.popleft()
        visit[now] = 1
        for next in nodes[now]:
            if visit[next] != 1:
                # next가 실내인 경우
                if items[next-1] == 0:
                    que.append(next)
                # next가 실외인 경우
                else:
                    count += 1
print(count)
