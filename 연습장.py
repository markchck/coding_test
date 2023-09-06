# n부터 왼쪽으로 키를 재면 n-1번 봐야하기 때문에 N^2이 됨
# 오른쪽으로 진행하면서 스택의 top보다 현재 숫자가 크면 넣고 스택 팝하고, 작으면 현재 숫자 append한다.
# 이렇게하면 그림자에 가려지는 놈들 9 5 7에서 5같은 놈들을 보지 않아도 되기 때문에 시간 단축된다.

import sys
input = sys.stdin.readline
N = int(input())
items = list(map(int, input().split()))
stack = []
answer = [0] * N
for i, item in enumerate(items):
    while stack:
        lastIndex, lastItem = stack[-1]
        if lastItem < item:
            stack.pop()
        else:
            answer[i] = lastIndex
            break
    stack.append((i+1, item))
print(*answer)
