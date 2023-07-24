# 검은색이 나오면 일단 다 바꾸면서 진행하다가 끝방에 도착하면 몇개를 바꿨는지 기록
# 깊게 파고들었다가 실패할수도 있으니 bfs로 진행
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
que = deque()
visit = [[-1] * N for _ in range(N)]
answer = []

map = []
for _ in range(N):
    map.append(input().strip())


def bfs(row, col):
    que.append((row, col))
    visit[row][col] = 0
    while que:
        r, c = que.popleft()
        if r == N-1 and c == N-1:
            return visit[r][c]
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]

            if (0 <= new_r < N and 0 <= new_c < N and visit[new_r][new_c] == -1):
                if (int(map[new_r][new_c]) == 1):
                    que.appendleft((new_r, new_c))
                    visit[new_r][new_c] = visit[r][c]
                else:
                    que.append((new_r, new_c))
                    visit[new_r][new_c] = visit[r][c] + 1


print(bfs(0, 0))


# import sys
# from collections import deque
# input = sys.stdin.readline
# N = int(input())
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# que = deque()
# visit = [[0] * N for _ in range(N)]
# answer = []
# tmp = 0
# map = []
# for _ in range(N):
#     map.append(input().strip())


# def bfs(row, col):
#     global tmp
#     que.append((row, col))
#     visit[row][col] = 1
#     while que:
#         r, c = que.popleft()
#         for i in range(4):
#             new_r = r + dr[i]
#             new_c = c + dc[i]
#             if new_r == N-1 and new_c == N-1:
#                 answer.append(tmp)

#             if (0 <= new_r < N and 0 <= new_c < N and visit[new_r][new_c] == 0):
#                 if (int(map[new_r][new_c]) == 1):
#                     que.appendleft((new_r, new_c))
#                     visit[new_r][new_c] = 1
#                 else:
#                     tmp += 1
#                     que.append((new_r, new_c))
#                     visit[new_r][new_c] = 1
#     return min(answer)


# print(bfs(0, 0))
