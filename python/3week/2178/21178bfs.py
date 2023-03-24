#좌표를 받으면 4방을 보는 로직
#1이면 count를 올리고 담에 볼 수 있도록 큐에 넣는다.
#1이 아니거나 음수이거나, N또는 M보다 큰 경우는 제외시킨다.

import sys
from collections import deque
input= sys.stdin.readline
N, M = map(int, input().split())
list_a = [list(map(int, input().rstrip())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
que = deque()

def bfs(row, col):
    que.append((row,col))
    while que:
        row, col = que.popleft()
        for i in range(4):
            new_row=row+dr[i]
            new_col=col+dc[i]

            # 0,0까지만 있고 -1,0은 없으니까 예외처리 필요하다.
            if new_row < 0 or new_row >= N or new_col <0 or new_col >= M:
                continue
            # 0인 곳은 갈 수 없으니까 예외처리해야함.
            if list_a[new_row][new_col] == 0:
                continue
            # 1일 때만 갈 수 있.
            if list_a[new_row][new_col]==1:
                # 다음에 방문해야하니 큐에 추가
                que.append((new_row,new_col))
                # 방문카운트 추가
                list_a[new_row][new_col] += list_a[row][col]
bfs(0,0)
print(list_a[N-1][M-1])