import sys
from collections import deque, defaultdict
que = deque()
visited = defaultdict(lambda: 0)
input = sys.stdin.readline

N, K = map(int, input().split())
que.append((N, 0))
result = sys.maxsize


def solution(n, k):
    global result
    while (que):
        now, count = que.popleft()
        visited[now] += 1
        if (now == K):
            result = min(result, count)
        else:
            arr = [now+1, now-1, now*2]
            for i in range(3):
                next = arr[i]
                if (0 <= next <= 100000 and (visited[next] == 0 or visited[next] == visited[now]+1)):
                    if (i == 2):
                        que.append((next, count))
                    else:
                        que.append((next, count+1))


solution(N, K)
print(result)
