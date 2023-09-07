# permutation은 한번 뽑은 숫자는 다시 못 쓴다는 제약이 있기 때문에 이 문제에선 쓸 수가 없다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
items = []
for i in range(M):
    answer = [0] * M
    for j in range(1, N+1):
        answer[i] = j
