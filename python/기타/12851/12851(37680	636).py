import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
que = deque()
que.append(N)

way = [0] * 100001
cnt, result = 0, 0
while que:
    now = que.popleft()
    temp = way[now]
    if (now == K):
        result = temp
        cnt += 1
        continue
    for next in [now-1, now+1, now*2]:
        if (0 <= next < 100001 and (way[next] == 0 or way[next] == way[now]+1)):
            way[next] = way[now]+1
            que.append(next)

print(result)
print(cnt)
