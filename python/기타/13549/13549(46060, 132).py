import sys
from collections import deque, defaultdict

que = deque()
visited = defaultdict(lambda: 0)
result = [0] * 100001
input = sys.stdin.readline

N, K = map(int, input().split())
que.append(N)
visited[N] = 1


def solution(n):
    while que:
        now = que.popleft()
        if (now == K):
            return
        for next in [now*2, now-1, now+1]:
            if (0 <= next < 100001 and visited[next] == 0):
                visited[next] = 1
                if next == now*2:
                    result[next] = result[now]
                else:
                    result[next] = result[now]+1
                que.append(next)


solution(N)
print(result[K])
