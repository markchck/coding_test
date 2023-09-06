import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
nodes = [[] for _ in range(M+1)]
count = [0] * (M+1)
que = deque()
result = [[0] * (M+1) for _ in range(M+1)]

for _ in range(M):
    X, Y, Z = map(int, input().split())
    nodes[Y].append((X, Z))
    count[X] += 1
# print(nodes)
for i in range(1, M+1):
    if (count[i] == 0):
        que.append(i)
while que:
    now = que.popleft()
    for node in nodes[now]:
        part, number = node
        if sum(result[now]) == 0:
            result[part][now] += number
        else:
            for i in range(1, M+1):
                result[part][i] += result[now][i] * number
        count[part] -= 1

        if count[part] == 0:
            que.append(part)
for index, answer in enumerate(result[N]):
    if answer != 0:
        print(index, answer)
