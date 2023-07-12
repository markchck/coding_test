import sys
from collections import deque
input = sys.stdin.readline
N, M = int(input()), int(input())
nodes = [[] for _ in range(M+1)]  # 관계를 표현한 노드
needs = [[0]*(N+1) for _ in range(N+1)]  # dp처럼 필요한 부품 수를 기록할 기록지
count = [0] * (N+1)  # 각 노드가 몇번 가리킴 당했는지 기록하는 count

que = deque()
for _ in range(M):
    X, Y, K = map(int, input().split())
    # 1이 5이 5를 만드는데 2개 필요하다로 표를 구성할거라서 node[x].append(Y,K)로하면 안됨
    nodes[Y].append((X, K))
    # [[], [(5, 2)], [(5, 2)], [(6, 3)], [(6, 4), (7, 5)], [(7, 2), (6, 2)], [(7, 3)], [], []]

    # nodes[X].append((Y, K))
    # [[], [], [], [], [], [(1, 2), (2, 2)], [(5, 2), (3, 3), (4, 4)], [(5, 2), (6, 3), (4, 5)], []]

    count[X] += 1  # 지목당한 X는 count를 올려준다.
    # [0, 0, 0, 0, 0, 2, 3, 3]

# count가 0인 즉 기본 부품들을 큐에 넣어준다.
# 큐에 넣는 이유는 기본 부품부터 시작해서 needs테이블을 채우려고
for i in range(1, N+1):
    if count[i] == 0:
        que.append(i)

while que:
    now = que.popleft()

    # (기본부품 또는 원랜 기본부품이 아니었으나 count를 하나씩 빼면서 기본부품화 된 것들인)now가 쓰이는 것들을 전부 대상으로 함 [(5, 2)], [(5, 2)], [(6, 3)]
    for next, next_need in nodes[now]:
        # 기본부품은 needs[now]의 모든 열이 0이라는 공통점이 있다. (.count(0)으로 0의 개수 센다.)
        if (needs[now].count(0) == (N+1)):
            # 원래 기본부품이면 needs테이블에 바로 필요한 부품 수 업데이트
            needs[next][now] += next_need  # 부품 5는 부품 1이 2개 필요하다를 기록

        # 0이 아닌게 있으면 현 부품이 중간부품인데 count가 -1씩 감소되어서 기본부품화 되었다는 소리
        else:
            # 기본부품화된 거를 만들기 위해 필요하다고 needs에 기록된 기본부품의 수에서 가중치를 곱하고 needs[next]자리에 기록

            # 7(next) 5(now) 2(next_need)를 예로 들면
            # 5번을 만드는데 필요한 부품들 기록된 것들에 전부 2만큼 멀티플을 곱해서
            # 7번 라인에 하나씩 넣는 중
            # 5를 만드는데 1이 2개, 2가 2개 필요하니까 7을 만드는데는 1이 4개, 2가 4개가 필요하다는 것을 기록 중
            for i in range(1, N+1):
                needs[next][i] += needs[now][i] * next_need

        # 위에서 중간부품을 기본부품으로 분해하는 작업이 끝났으니 화살표 맞은 부품의 차수 -1
        count[next] -= 1
        # 만약 차수가 0이되면 기본부품화 되었다는 의미이니까 큐에 넣기
        if count[next] == 0:
            que.append(next)

for x in enumerate(needs[N]):
    if x[1] > 0:
        print(*x)
