import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())
visited = defaultdict(lambda: 0)


def solution(n, k):
    que = deque([(n, 0)])
    while (que):
        now, count = que.popleft()
        if (now == k):
            return count
        else:
            if (now < 100001 and visited[now] == 0):
                visited[now] = 1
                count += 1
                que.append((now+1, count))
                que.append((now*2, count))
                que.append((now-1, count))


print(solution(N, K))
