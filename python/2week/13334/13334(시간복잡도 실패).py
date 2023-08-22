# 시작점을 바꿔가면서 선분을 배치하고 시작점 + 선분길이가 끝점이 될텐데 그 끝점보다 작은놈들을 전부 카운팅
# 다음 시작점에도 똑같이 적용하면서 기존 count보다 크기 비교해서 더 큰 경우만 다시 Count라고 한다.

#! 사무실 집 모두 포함해야한다 어느 하나만 포함해도 되는게 아니라

import sys
input = sys.stdin.readline

items = []
N = int(input())
for i in range(N):
    A = (tuple(map(int, input().split())))
    A = tuple(sorted(A))
    items.append(A)
D = int(input())


answer = 0
new_items = set(items)
new_items = list(new_items)

items.sort(key=lambda x: (x[0], x[1]))

for new_item in new_items:
    # 선분의 시작점이 될 수 있는 것들의  리스트가 new_items(items의 중복되는 놈들을 제거한 상태)
    start = new_item[0]
    # end = new_item[1]

    line_start, line_end = [start, start+D]

    count = 0
    for i in range(len(items)):
        home, office = items[i]

        # 선분보다 집과 오피스 차이가 커버리면 죽었다 깨도 집, 오피스 모두 들어올 수는 없다.
        if (office-home) > D:
            continue
        if line_start <= home and office <= line_end:  # 선분 사이에 home, office  모두 들어오는 경우
            count += 1
    answer = max(answer, count)
print(answer)
