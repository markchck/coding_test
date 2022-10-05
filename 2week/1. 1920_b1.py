# https://www.acmicpc.net/problem/1920
# 29일 오후 3시에 시작
# 시간초과 뜸.
N = int(input())
A_list = list(map(int, input().split(" ")))
M = int(input())
B_list = list(map(int, input().split(" ")))

for b in B_list:
  if b in A_list:
    print(1)
  else:
    print(0)
