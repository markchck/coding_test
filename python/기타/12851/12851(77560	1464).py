import sys
from collections import defaultdict, deque
input = sys.stdin.readline
que = deque()
N, K = map(int, input().split())
visited = defaultdict(lambda: 0)
time = sys.maxsize
case = 0

que.append((N, 0))


def solution(n, k):
    global time, case
    while (que):
        now, count = que.popleft()
        visited[now] += 1
        if (now == k and count <= time):
            time = min(count, time)
            case += 1
        else:
            for next in [now*2, now+1, now-1]:
                if (0 <= next <= 100000 and (visited[next] == 0 or visited[next] == visited[now]+1)):
                    que.append((next, count+1))


solution(N, K)

print(time)
print(case)
