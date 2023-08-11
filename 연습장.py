import sys
input = sys.stdin.readline
N, M = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(row, col):
    stack = []
    stack.append((row, col))
    while stack:
        r, c = stack.pop()
        if items[r][c] > 0 and visited[r][c] == 0:
            visited[r][c] = 1
            iceCount = 0
            for i in range(4):
                new_r = r+dr[i]
                new_c = c+dc[i]
                if visited[new_r][new_c] == 0:
                    if items[new_r][new_c] <= 0:
                        iceCount += 1
                    else:
                        stack.append((new_r, new_c))
            items[r][c] -= iceCount
            if items[r][c] <= 0:
                ice[(r, c)] = 0


ice = {}
for i in range(1, N-1):
    for j in range(1, M-1):
        if items[i][j] != 0:
            ice[(i, j)] = 1

year = 0
while sum(ice.values()) > 0:
    dfs_count = 1
    visited = [[0] * M for _ in range(N)]
    for key, value in ice.items():
        row, col = key
        if visited[row][col] == 0 and value != 0:
            if dfs_count == 2:
                print(year)
                break
            else:
                if visited[row][col] == 0 and items[row][col] != 0:
                    dfs(row, col)
                    dfs_count += 1
    else:
        year += 1
        continue
    break
else:
    print(0)
