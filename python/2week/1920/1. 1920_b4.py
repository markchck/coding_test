# https://www.acmicpc.net/problem/1920

# set이라는 자료구조로 데이터를 잘 정리해놓고 그걸 불러내면 통과됨.
# 이진탐색을 의도한 문제이지만 이런 관점으로도 문제를 풀 수 있다.

N = int(input())
A_list = set(map(int, input().split(" ")))
M = int(input())
B_list = list(map(int, input().split(" ")))

for b in B_list:
  if b in A_list:
    print(1)
  else:
    print(0)