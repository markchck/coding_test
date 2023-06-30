import heapq
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

nodes = [[] for _ in range(N+1)]
result = [10**9]*(N+1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    nodes[start].append((cost, end))

# [[], [(2, 2), (3, 3), (1, 4), (10, 5)],   [(2, 4)],   [(1, 4), (1, 5)],   [(3, 5)],   []]
startCity, endCity = map(int, input().split())

result[startCity] = 0


def bfs(startCity, endCity):
    que = []
    heapq.heappush(que, (result[startCity], startCity))
    while que:
        curCost, currentCity = heapq.heappop(que)

        if (result[currentCity] < curCost):
            continue

        for itr in nodes[currentCity]:
            addedCost, nextCity = itr[0], itr[1]
            newCost = curCost + addedCost

            if (newCost < result[nextCity]):
                result[nextCity] = newCost
                heapq.heappush(que, (newCost, nextCity))
    return print(result[endCity])


bfs(startCity, endCity)
