# 다음 타켓팅을 선정할 때 최선의 선택을 할거니까 힙을 쓸거고
# 전체를 다 가봐야하니까 bfs나 dfs를 쓸거야
# 깊게 들어갔다가 실패하는 리스크를 줄이기 위해 bfs로 탐색할거야.

import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# 관계설정
# 단방향이기 때문에 visited 여부를 체킹하지는 않을거고
nodes = [[] for _ in range(N+1)]
distance = [10**9] * (N+1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    # cost를 기준으로 힙을 사용할 예정이라서 cost를 앞에 놓을거
    nodes[start].append([cost, end])

startCity, endCity = map(int, input().split())


def bfs(startCity, endCity):
    que = []
    heapq.heappush(que, [0, startCity])
    while que:
        cost, now = heapq.heappop(que)  # cost, now =[0,1] 이게 됨?
        if (distance[now] < cost):
            continue
        for next in nodes[now]:
            new_cost = cost+next[0]
            if (new_cost < distance[next[1]]):
                distance[next[1]] = new_cost
                heapq.heappush(que, [new_cost, next[1]])
    print(distance[endCity])


bfs(startCity, endCity)
