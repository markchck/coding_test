# permutation은 한번 뽑은 숫자는 다시 못 쓴다는 제약이 있기 때문에 이 문제처럼 여번 써야하는 상황에선 쓸 수가 없다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())


def dfs():
    if len(items) == M:
        print(*items)
        return
    else:
        for i in range(1, N+1):
            items.append(i)
            dfs()
            items.pop()


items = []
dfs()
