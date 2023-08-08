import collections
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = collections.defaultdict(list)
visited = [0] * (n+1)

for i in range(m):
    u, v, cost = map(int, input().split())
    nodes[u].append([cost, u, v])
    nodes[v].append([cost, v, u])
# print(nodes)
# defaultdict(<class 'list'>, {1: [[1, 1, 2], [3, 1, 3]], 2: [[1, 2, 1], [2, 2, 3]], 3: [[2, 3, 2], [3, 3, 1]]})


def prim(nodes, start):
    visited[start] = 1
    candidate = nodes[start]
    heapq.heapify(candidate)
    # print(candidate) #[[1, 1, 2], [3, 1, 3]]
    mst = []
    answer = 0
    while candidate:
        cost, u, v = heapq.heappop(candidate)
        if visited[v] == 0:
            visited[v] = 1
            mst.append((u, v))
            answer += cost
            for node in nodes[v]:
                next_v = node[2]
                if visited[next_v] == 0:
                    heapq.heappush(candidate, node)
    return answer


print(prim(nodes, 1))
