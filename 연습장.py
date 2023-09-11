from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    que = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[0] * (M) for _ in range(N)]
    que.append((0, 0))
    visited[0][0] = 1

    while que:
        r, c = que.popleft()
        if r == N-1 and c == M-1:
            return visited[r][c]
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < M and maps[new_r][new_c] == 1 and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = visited[r][c] + 1
                que.append((new_r, new_c))
    return -1


solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
         1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
