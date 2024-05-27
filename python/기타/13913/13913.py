import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
que = deque()
que.append(N)
visited = defaultdict(lambda: -1)
result = [0] * 100001
arr = []


def recursion(now, count):
    if (count == 0):
        return
    else:
        count -= 1
        arr.append(now)
        return recursion(visited[now], count)


def solution(n, k):
    while (que):
        now = que.popleft()
        if (now == k):
            recursion(now, result[now]+1)
            return
        else:
            for next in [now*2, now+1, now-1]:
                if (0 <= next <= 100000 and visited[next] == -1):
                    visited[next] = now
                    result[next] = result[now]+1
                    que.append(next)


solution(N, K)
print(result[K])
print(*arr[::-1])
