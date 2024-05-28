import sys
from collections import deque
# sys.setrecursionlimit(10**6)#재귀 최대 깊이 설정

input = sys.stdin.readline
MAX = 100001
n, k = map(int, input().split())
dq = deque()
dist = [-1]*MAX
route = [-1]*MAX


def track(o, d):
    routes = []
    dest = k
    routes.append(k)
    while dest != o:
        routes.append(route[dest])
        dest = route[dest]
    routes.reverse()
    print(' '.join(map(str, routes)))


'''
#역추적 방법2) 재귀
def track(o,d):
    if o!=d:
        track(o,route[d])
        print(d,end=' ')
    else:
        print(o,end=' ')
'''
dist[n] = 0  # 초기 위치(수빈's)
route[n] = n
dq.append(n)
while dq:
    x = dq.popleft()
    if x == k:  # 도착
        print(dist[k])
        track(n, k)
        break
    for nx in [x+1, x-1, 2*x]:  # 가능한 3가지 행동
        if 0 <= nx < MAX and dist[nx] == -1:
            dist[nx] = dist[x]+1
            route[nx] = x  # 이전 정점이 무엇이었는지 기록
            dq.append(nx)
