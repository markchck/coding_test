# https://www.youtube.com/watch?v=GyuGUhWOKXA
# 대체 백트래킹이 뭐가 다르길래 1208ms을 60ms으로 줄임?
# https://zu-techlog.tistory.com/62

import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_result = -int(1e9)
min_result = int(1e9)


def recursion(add, sub, mul, div, sum, idx):
    global max_result, min_result
    if idx == N:
        max_result = max(max_result, sum)
        min_result = min(min_result, sum)
        return
    else:
        if add:
            recursion(add - 1, sub, mul, div, sum+numbers[idx], idx + 1)
        if sub:
            recursion(add, sub - 1, mul, div, sum-numbers[idx], idx + 1)
        if mul:
            recursion(add, sub, mul - 1, div, sum*numbers[idx], idx + 1)
        if div:
            recursion(add, sub, mul, div - 1, int(sum/numbers[idx]), idx + 1)


recursion(add, sub, mul, div, numbers[0], 1)
print(max_result, min_result)
