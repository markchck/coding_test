import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, K = map(int, input().split())
que = deque()
que.append(N)
visited = defaultdict(lambda: -3)
count = [0] * 100001
arr = []


def recursion(now, count):
    if (count == -1):
        return
    else:
        count -= 1
        arr.append(now)
        return recursion(visited[now], count)


def solution(n, k):
    while que:
        now = que.popleft()
        if (now == k):
            recursion(now, count[now])
            return
        else:
            for next in [now+1, now-1, now*2]:
                if (0 <= next <= 100000 and visited[next] == -3):
                    visited[next] = now
                    # if now != 0:
                    count[next] = count[now]+1
                    que.append(next)


solution(N, K)
print(count[K])
print(*arr[::-1])
