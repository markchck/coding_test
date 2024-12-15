

import sys
input = sys.stdin.readline

# 입력받고
N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(input().strip().split())

# 덩어리를 카운트하는 작업
#   루프를 돌면서 덩어리가 몇 개인지 체크


def countParts(maps):
    pass


def melting():
    pass

# 덩어리 개수가 2개 미만이면 while로 루프 계속 돔.
#   빙산이 다 녹으면 0을 출력하고 루프 탈출
#   year 변수를 +1 증가시킨다.
#   빙산을 녹인다.


def solution(maps):
    year = 0
    while True:
        count = countParts(maps)
        if (count == 0):
            return 0
        if (count >= 2):
            return year
        else:
            year += 1
            melting()


print(solution(maps))
