from collections import deque
nowL = '*'
nowR = '#'
pressL = [1, 4, 7, "*"]
pressR = [3, 6, 9, "#"]
press = [2, 5, 8, 0]
# que = deque()
items = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]


# bfs로 탐색을 진행하고 target까지 도달하는 거리를 리턴하면됨.
def bfs(now, target):
    que = deque()
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        for j in range(3):
            if items[i][j] == now:
                now_r, now_c = i, j
            if items[i][j] == target:
                tar_r, tar_c = i, j

    que.append((now_r, now_c))
    visited = [[0] * 3 for i in range(4)]
    while que:
        now_r, now_c = que.popleft()

        # if now_r == tar_r and now_c == tar_c:
        #     return visited[now_r][now_c]
        # else:
        #     for i in range(4):
        #         new_r = now_r + dr[i]
        #         new_c = now_c + dc[i]
        #         if 0 <= new_r < 4 and 0 <= new_c < 3 and visited[new_r][new_c] == 0:
        #             que.append((new_r, new_c))
        #             visited[new_r][new_c] = visited[now_r][now_c] + 1

        for i in range(4):
            new_r = now_r + dr[i]
            new_c = now_c + dc[i]
            if 0 <= new_r < 4 and 0 <= new_c < 3 and visited[new_r][new_c] == 0:
                if new_r == tar_r and new_c == tar_c:
                    #  visited[new_r][new_c] == 0: 조건에 따라서
                    # 새로 개척할 곳은 항상 visited가 0인데 그걸 출력해버리면 어캄.
                    # visited[now_r][now_c]에서 한 칸 더 갔으니까 +1을 리턴해야지
                    return visited[now_r][now_c] + 1
                que.append((new_r, new_c))
                visited[new_r][new_c] = visited[now_r][now_c] + 1


def solution(numbers, hand):
    global pressL, pressR, press, nowR, nowL
    answer = ''
    for num in numbers:
        # 1,4,7인 경우
        if num in pressL:
            answer += 'L'
            nowL = num
        # 3,6,9인 경우
        elif num in pressR:
            answer += 'R'
            nowR = num
        # 2,5,8,0인 경우
        else:
            countR = bfs(nowR, num)
            countL = bfs(nowL, num)
            if countR > countL:
                answer += 'L'
                nowL = num
            elif countR < countL:
                answer += 'R'
                nowR = num
            else:
                if hand == "right":
                    answer += 'R'
                    nowR = num
                else:
                    answer += 'L'
                    nowL = num
    print(answer)
    return (answer)


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
