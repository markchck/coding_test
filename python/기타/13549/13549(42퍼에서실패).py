import sys
from collections import deque, defaultdict

que = deque()
visited = defaultdict(lambda: 0)
input = sys.stdin.readline
max = 100001

N, K = map(int, input().split())
que.append((N, 0))
visited[N] = 1


def solution(n):
    while que:
        now, count = que.popleft()
        if (now == K):
            return count
        else:
            arr = [now*2, now+1, now-1]
            for i in range(3):
                next = arr[i]
                if (0 <= next <= 100000 and visited[next] == 0):
                    if (i == 0):
                        visited[next] = 0
                        que.append((next, count))
                    else:
                        visited[next] = 1
                        que.append((next, count+1))

                # for next in [now*2, now-1, now+1]:
                #     if (0 <= next < max and (visited[next] == 0)):
                #         visited[next] = 1
                #         if next != now*2:
                #             count = count+1

                #         if visited[next] == 0:
                #             que.append((next, count))


print(solution(N))
