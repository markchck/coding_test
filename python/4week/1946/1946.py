# 서류 기준으로 정렬
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    items = []
    for j in range(N):
        items.append(list(map(int, input().split())))
    items.sort()
    # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]] /// [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
    que = deque(items)
    interview = que.popleft()[1]
    count = 1
    for item in que:
        n_interview = item[1]
        if interview > n_interview:
            count += 1
            interview = n_interview

    print(count)


# # 서류 기준으로 정렬
# import sys
# from collections import deque

# input = sys.stdin.readline
# T = int(input())
# for i in range(T):
#     N = int(input())
#     items = []
#     for j in range(N):
#         items.append(list(map(int, input().split())))
#     items.sort()
#     que = deque(items)
#     # [[1, 4], [2, 3], [3, 2], [4, 1], [5, 5]] /// [[1, 4], [2, 5], [3, 6], [4, 2], [5, 7], [6, 1], [7, 3]]
#     answer = []
#     count = 0
# while que:
#     paper, interview = que.popleft()
#     for item in que:
#         n_paper, n_interview = item
#         # 이미 answer에 들어온 놈들도 탈락되는 경우(4,2와 7,3의 관계처럼)가 있다.
#         if n_paper < paper or n_interview < interview:
#             if [n_paper, n_interview] not in answer:
#                 count += 1
# # 이미 answer에 들어간 7,3을 4,2때문에 answer에서 제외시켜야하는 방향으로 로직을 짜면 어렵다.
# # 때문에 answer에 뭘 넣기 전에 따져가면서 넣어야하는거임.
# # 그러려면 answer에 들어가는 놈이 잇으면 그놈이 들어가면서 기존의 커트라인보다 더 어렵게 바꾸고 들어가면 된다.
