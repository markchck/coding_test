# for문을 돌면서 썩은 토마토가 있으면 그때마다 그 토마토의 좌표를 큐에 넣고
# 큐가 빌 때까지 while문을 반복
# 큐에서 하나 팝해서 상, 하 , 좌, 우, 앞, 뒤를
# for문을 다 돌면 하루가 지난 것으로 보고 count를 1 추가

from collections import deque
import sys
input = sys.stdin.readline
M, N, H = map(int, input().split())
items = [[list(map(int, input().split())) for _ in range(N)] for i in range(H)]
que = deque()
notYet = []
empty = []

dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
answer = 0
for h in range(len(items)):
    for r in range(len(items[h])):
        for c in range(len(items[h][r])):
            if items[h][r][c] == 1:  # 익은 토마토
                que.append((h, r, c, 0))
            elif items[h][r][c] == 0:
                notYet.append((h, r, c, 0))
            else:
                empty.append((h, r, c, 0))

if len(notYet) == 0:
    print(0)
else:     # 토마도가 모두 익지 못하는 상황이거나 / 시간이 지나면 익을 수 있는 상황
    count = -1000
    while que:
        h, r, c, day = que.popleft()
        count = max(count, day)
        for i in range(6):
            new_h = h + dh[i]
            new_r = r + dr[i]
            new_c = c + dc[i]

            if 0 <= new_h < H and 0 <= new_c < M and 0 <= new_r < N and items[new_h][new_r][new_c] == 0:
                # 토마토를 익히고
                items[new_h][new_r][new_c] = 1
                que.append((new_h, new_r, new_c, day+1))

    answer = count

    for h in range(len(items)):
        for r in range(len(items[h])):
            for c in range(len(items[h][r])):
                if items[h][r][c] == 0:
                    answer = -1
    print(answer)
