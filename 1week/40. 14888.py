# https://www.acmicpc.net/problem/14888

N = int(input())
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))

from itertools import permutations
for i in range(N-1):
    if (list_2[i] != 0):
        # 개수정렬을 써야하는듯하다
        
