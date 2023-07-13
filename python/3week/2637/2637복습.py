# 뭐 다음에 뭐다 식의 순서가 있다? -> 위상정렬

from collections import deque
import sys
input = sys.stdin.readline
que = deque()

N = int(input())
M = int(input())

# 1번부품은 5번에 2개 필요라는 관계를 기록할 수 있는 자료구조 선언 (환산을 한 것은 아니다.)
nodes = [[] for _ in range(M+1)]

# 하트 받은 횟수를 기록할 수 있는 자료구조 선언 (5번은 1번에게 하트를 받음)
count = [0] * (M+1)

# 부품당 몇 개의 기본 부품이 필요한지 '환산'한 결과를 기록하는 자료구조 선언
# 5번은 1번이 2개 필요하고 7번은 5번이 2개 필요하면 7번은 1번이 몇 개 필요한지 환산이 필요함
result = [[0] * (M+1) for _ in range(M+1)]

# 인풋값들 자료구조에 기록
for _ in range(M):
    X, Y, Z = map(int, input().split())
    # node간에 관계 설정
    nodes[Y].append((X, Z))
    # 하트 받은 횟수 설정
    count[X] += 1

# 환산 작업을 위해 큐에 하트가 0인 기본 부품들 투입
for i in range(1, M+1):
    if (count[i] == 0):
        que.append(i)

# 기본부품들부터 꺼내서 필요한 부품 수를 환산한 기록지에 적기 시작
while que:
    now = que.popleft()
    for node in nodes[now]:  # 1번 부품이 들어가는 놈들 하나씩 살펴보자
        next, number = node
        # count가 0인 경우는 5번처럼 중간 부품인 놈이 기본부품으로 환산 된 경우가 있고 1번처럼 원래부터 기본부품인 놈이 있다.
        # 5처럼 기본부품으로 환산된 놈은 환산된 기본 부품수에 * number 한 만큼을 result[now][next]에 넣어야함.
        # 7은 5가 2개 필요하고 5는 1이 2개니까 2*2가 7에 들어가야함

        if sum(result[now]) == 0:  # 원래부터 기본부품인 경우는 result가 모두 0일 것임
            result[next][now] += number
            # 기본부품을 result기록지에 기록했으니까 count -1
        else:
            for i in range(1, M+1):
                result[next][i] += result[now][i]*number

        count[next] -= 1

        if count[next] == 0:
            que.append(next)

for index, answer in enumerate(result[N]):
    if (answer != 0):
        print(index, answer)
