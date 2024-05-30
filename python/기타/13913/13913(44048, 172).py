import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, K = map(int, input().split())
que = deque()
que.append((N, 0))
visited = defaultdict(lambda: -3)
arr = []


def solution(n, k):
    while que:
        now, count = que.popleft()
        if (now == k):
            print(count)
            arr.append(now)
            while count > 0:
                count -= 1
                arr.append(visited[now])
                now = visited[now]
            return
        else:
            for next in [now*2, now+1, now-1]:
                if (0 <= next <= 100000 and visited[next] == -3):
                    visited[next] = now
                    que.append((next, count+1))


solution(N, K)
print(*arr[::-1])
