from collections import deque


def solution(m, n, puddles):

    dr = [0, 1]
    dc = [1, 0]
    que = deque()

    def bfs(col, row, count):
        que.append((col, row))
        while que:
            col, row = que.popleft()
            for i in range(2):
                new_col = col + dc[i]
                new_row = row + dr[i]

                if (new_col <= m and new_row <= n and [new_col, new_row] not in puddles):
                    for puddle in puddles:
                        if puddle == [new_col, new_row]:
                            break
                    if ([new_col, new_row] == [m, n]):
                        count += 1
                    else:
                        que.append((new_col, new_row))

        return count % 1000000007
    return bfs(1, 1, 0)


print(solution(4, 3, [[2, 2]]))
