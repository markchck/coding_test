import sys
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]


def bear(r, c):
    visited[r][c] = 1
    bear_que.append((r, c))
    while bear_que:
        bearq_len = len(bear_que)
        while bearq_len:
            # new_r, new_c = bear_que.popleft()
            bear_r, bear_c = bear_que.popleft()
            for i in range(4):
                new_r = bear_r + dr[i]
                new_c = bear_c + dc[i]
                if 0 <= new_r < R and 0 <= new_c < C:
                    if items[new_r][new_c] == '.' and visited[new_r][new_c] == 0:
                        visited[new_r][new_c] = visited[bear_r][bear_c] + 1
                        bear_que.append((new_r, new_c))
                    elif items[new_r][new_c] == 'D':
                        # 최초 bear가 있는 visited를 0이 아닌1로해줫기 때문에 visited[new_r][new_c]해서 -1하지 않고 visited[r][c]로해도 됨.
                        print(visited[bear_r][bear_c])
                        return
            bearq_len -= 1
        water()
    print("KAKTUS")
    return


def water():
    w_len = len(water_que)
    while w_len:
        r, c = water_que.popleft()
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < R and 0 <= new_c < C:
                if items[new_r][new_c] == '.':
                    items[new_r][new_c] = '*'
                    water_que.append((new_r, new_c))
        w_len -= 1


R, C = map(int, input().split())

items = []
for i in range(R):
    items.append(list(map(str, input())))
    # items.append(input())

visited = [[0]*C for _ in range(R)]
bear_que, water_que = deque(), deque()

for r in range(R):
    for c in range(C):
        if items[r][c] == 'S':
            bear_r, bear_c = r, c
        elif items[r][c] == '*':
            water_que.append((r, c))
water()
bear(bear_r, bear_c)
