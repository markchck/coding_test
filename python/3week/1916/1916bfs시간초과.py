# --------------------------------------------
# 메모리초과
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
que = deque()

nodes = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for _ in range(M):
    a, b, cost = map(int, input().split())
    # [[],    [(2, 2), (3, 3), (4, 1), (5, 10)],   [(4, 2)],    [(4, 1), (5, 1)],    [(5, 3)],    []]
    nodes[a].append([b, cost])

start, end = map(int, input().split())

# 최종목적지에 도착할 수 있는 경로들의 비용을 넣는 배열
result = []


def bfs(x):
    parents[x] = x
    que.append((x, 0))
    while que:
        num, cost = que.popleft()
        if num == end:
            result.append(cost)
            continue

        for info in nodes[num]:
            destination = info[0]
            new_cost = cost + info[1]
            que.append((destination, new_cost))
    return print(min(result))


bfs(start)


# ---------------------------------------------
# 시간초과

# # 매순간 최선의 선택을하면 최소비용이 나오지 않을까?
# # 목적지에 도착했는지 체킹하고
# # 왜 BFS인지는 모르겠음 (BFS를 써야하는 이유가 꼭 필요함. 시험에는 BFS라고 안나올테니까)
# # 어떤 경로로 가야 최적인지 미래를 볼 수 없기 때문에 다 가봐야함. (가장 싼데로만 가다가 도착지에 못도착하면 안되니까)
# # 여러 경로들 중 도착지에 도착하는 경우들을 따로 배열에 넣고 그 배열의 최소값을 출력하면 되겠다

# import sys
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# que = deque()

# nodes = [[] for _ in range(N+1)]
# parents = [0] * (N+1)

# for _ in range(M):
#     a, b, cost = map(int, input().split())
#     # [[],    [(2, 2), (3, 3), (4, 1), (5, 10)],   [(4, 2)],    [(4, 1), (5, 1)],    [(5, 3)],    []]
#     nodes[a].append([b, cost])

# start, end = map(int, input().split())

# # 최종목적지에 도착할 수 있는 경로들의 비용을 넣는 배열
# result = []


# def bfs(x):
#     parents[x] = x
#     que.append(x)
#     while que:
#         num = que.popleft()
#         for info in nodes[num]:
#             destination = info[0]
#             cost = info[1]

#             # # 방문여부부터 체킹 (단방향이기 때문에 방문여부 체킹 안해야함. 1->2갔다고 2를 체킹하면 3->2는 못가게 됨)
#             # if (parents[destination] == 0):
#             #     parents[destination] = destination

#             # 최종 목적지 도착여부 체킹 (도착했으면 result배열에 추가)
#             if (destination == end):
#                 result.append(cost)
#             else:
#                 # 다음 노드를 que에 추가하고
#                 que.append(destination)

#                 # 다음 노드들의 비용을 일괄 cost만큼 추가 (탐색에 실패했으니 비용이 늘어나야함)
#                 for node in nodes[destination]:
#                     node[1] += cost
#     return print(min(result))


# bfs(start)
