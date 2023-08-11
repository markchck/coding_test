# 이걸 어떻게 코딩으로 풀 수 있다는 거냐라는 생각이 드는 유형임
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
items = []
for _ in range(N):
    items.append(list(map(int, input().split())))

ice = {}  # 좌표(x,y)에 해당하는 value를 O(1)로 탐색해서 바꾸기 위해 딕셔너리로 선언함.
# 첫행, 끝행, 첫열, 끝열은 0이라고 했기때문에 제외하기위해서 1부터 시작하고 N-1, M-1함.
for i in range(1, N-1):
    for j in range(1, M-1):
        if items[i][j] != 0:
            ice[(i, j)] = 1  # (i,j)가 빙산인 경우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dfs(r, c):
    linked_ice = [(r, c)]
    while linked_ice:
        now_r, now_c = linked_ice.pop()  # 스택을 쓰기 때문에 dfs
        if visited_ice[now_r][now_c] == False:
            visited_ice[now_r][now_c] = True
            water_count = 0
            for i in range(4):
                next_r = now_r + dr[i]
                next_c = now_c + dc[i]
                # 이 코드가 없으면... (1이다가 0이된 빙하 a가 있다고 쳐. 근데 그 옆에 있던 빙하 b는 a가 0이된 이후니까 a도 watercount에 포함하게 되어버림.)
                if visited_ice[next_r][next_c] == False:
                    if items[next_r][next_c] <= 0:  # 만약 next가 물이면?
                        water_count += 1
                    else:
                        # 물이 아니면 인접한 빙하로 추가해준다.
                        linked_ice.append((next_r, next_c))
            items[now_r][now_c] -= water_count  # 사방을 본 이후 물 수만큼 빼주고
            if items[now_r][now_c] <= 0:
                ice[(now_r, now_c)] = 0  # 빙하를 물로 바꿔준다.


year = 0
while sum(ice.values()) > 0:  # 녹일 얼음이 있을 때까지만 반복 (.values()하면 모든 value들의 합 )
    dfs_count = 1
    visited_ice = [[False] * M for i in range(N)]
    for key, value in ice.items():  # .items()하면 모든 (key,value)가 튜플에 묶인 채로 배열에 담겨서 나옴 (이터레이팅 할 수 있다는 뜻)
        row, col = key
        # 현재 좌표가 아직 방문하지 않은 곳이고 동시에 빙산인 경우만 빙산 녹이러 dfs 들어가야함.
        if value and visited_ice[row][col] == False:
            # 이 구문이 없으면 for문이 두 번째 돌 때 dfs_count += 1 때문에 dfs_count가 2가 되면서 break를 타게 됨. year는 0인 상태로.
            if dfs_count == 2:
                print(year)
                break

            dfs(row, col)
            dfs_count += 1  # DFS 함수가 한번 호출되면, 연결된 얼음을 stack에 담아가면서 탐색을 이어가기 때문에 연결된 빙산은 모두 돌고 함수가 종료된다. 따라서, 한 해에 DFS가 호출된 횟수가 빙산 덩어리의 수
    else:  # for반목문이 모두 돌고 나서 실행되는 구문
        year += 1
        continue  # while 반복문이 다시 돈다.
    break  # while문을 종료한다.
else:  # while 문을 다 돌고도 break되지 않을 때 실행된다.
    print(0)
