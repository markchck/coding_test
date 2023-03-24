#좌표를 받으면 4방을 보는 로직
#1이면 count를 올리고 담에 볼 수 있도록 큐에 넣는다.
#1이 아니거나 음수이거나, N또는 M보다 큰 경우는 제외시킨다.
#실패함!!!
import sys
from collections import deque
input= sys.stdin.readline
N, M = map(int, input().split())
list_a = [list(map(int, input().rstrip())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(row,col):
    if visit[row][col] ==0:
        visit[row][col] = 1
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]

            if new_col < 0 or new_col >=M or new_row <0 or new_row >=N:
                continue
            if list_a[new_row][new_col] == 0:
                continue
            if list_a[new_row][new_col] == 1:
                list_a[new_row][new_col] += list_a[row][col]
                dfs(new_row,new_col)
dfs(0,0)
print(list_a[N-1][M-1])