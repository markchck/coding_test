# def solution(park, routes):
#     r,c,R,C = 0,0,len(park),len(park[0]) # r,c : S위치 / R,C : 보드경계
#     move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)}
#     for i,row in enumerate(park): # 시작점 찾기
#         if "S" in row:
#             r,c = i,row.find("S")
#             break

#     for route in routes:
#         dr,dc = move[route[0]] # 입력받는 route의 움직임 방향
#         new_r,new_c = r,c # new_r,new_c : route 적용 후 위치
#         for _ in range(int(route[2])):
#             # 한칸씩 움직이면서, 보드 안쪽이고 "X"가 아니라면 한칸이동
#             if 0<=new_r+dr<R and 0<=new_c+dc<C and park[new_r+dr][new_c+dc] != "X":
#                 new_r,new_c = new_r+dr,new_c+dc
#             else: # 아니라면 처음 위치로
#                 new_r,new_c = r,c
#                 break
#         r,c = new_r,new_c # 위치 업데이트

#     return [r,c]


# def solution(park, routes):

#     avoidIndex = []

#     # 공원 시작점, 장애물 지도화하기(index)
#     # for r in range(len(park)):
#     #     if (park[r].find("S") >= 0):
#     #         startingIndex = [r, int(park[r].find("S"))]
#     #     if (park[r].find("X") >= 0):
#     #         avoidIndex.append([r, int(park[r].find("X"))])

#     for r in range(len(park)):
#         if (park[r].find("S") >= 0):
#             startingIndex = [r, int(park[r].find("S"))]

#         for i in range(len(park[r])):
#             if (park[r][i] == 'X'):
#                 avoidIndex.append([r, i])

#     maxIdxOfCol = len(park[0]) - 1
#     maxIdxOfRow = len(park) - 1

#     for route in routes:
#         op, n = route.split(' ')
#         n = int(n)
#         # 공원의 범위를 넘어가는지 체크

# # 쩜프를 해서 가는게 아니니까.. 중간에 장애물에 걸리는 것을 막아줘야하네?!
#         if (op == 'E'):
#             if (startingIndex[1] + n <= maxIdxOfCol):

#                 # 1씩 증가해야하는데 2번째 턴에서 2가 증가해버리잖음..
#                 for i in range(1, n+1):
#                     if ([startingIndex[0], startingIndex[1]+i] in avoidIndex):
#                         break
#                     else:
#                         startingIndex[1] += 1
#             continue

#         if (op == 'W'):
#             if (startingIndex[1] - n >= 0):
#                 for i in range(1, n+1):
#                     if ([startingIndex[0], startingIndex[1]-i] in avoidIndex):
#                         break
#                     else:
#                         startingIndex[1] -= -1
#             continue
#         if (op == 'S'):
#             if (startingIndex[0] + n <= maxIdxOfRow):
#                 for i in range(1, n+1):
#                     if ([startingIndex[0]+i, startingIndex[1]] in avoidIndex):
#                         break
#                     else:
#                         startingIndex[0] += 1
#             continue
#         if (op == 'N'):
#             if (startingIndex[0] - n >= 0):
#                 for i in range(1, n+1):
#                     if ([startingIndex[0] - i, startingIndex[1]] in avoidIndex):
#                         break
#                     else:
#                         # startingIndex[0] = -i
#                         startingIndex[0] -= -1
#             continue
#     return startingIndex


def solution(park, routes):
    # park 최대 넓이 설정
    x, y, X, Y = 0, 0, len(park), len(park[0])

    # 동서남북
    EWSN = {
        'E': (0, 1),
        'W': (0, -1),
        'S': (1, 0),
        'N': (-1, 0)
    }

    # 시작점 위치
    for i, row in enumerate(park):
        if "S" in row:
            r, c = i, row.find("S")
            break

    for route in routes:
        dr, dc = EWSN[route[0]]
        new_r, new_c = r, c
        # 이동
        for step in range(int(route[2])):
            # 제약조건
            if (0 <= new_r+dr < Y and
                0 <= new_c+dc < X and
                park[new_r+dr][new_c+dc] != 'X'
                ):
                new_r, new_c = new_r+dr, new_c+dc
            else:
                new_r, new_c = r, c
                break
        r, c = new_r, new_c

    return [r, c]


park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]

solution(park, routes)
