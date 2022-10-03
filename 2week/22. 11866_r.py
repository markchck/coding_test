# https://www.acmicpc.net/problem/11866
# 9시 14분 시작
# 너무 어렵다..

from collections import deque
import sys

# 입력
N, K=map(int, (sys.stdin.readline().split(" ")))
print("<",end='')

# 초깃값 셋팅
deq = []
for itr_N in range(N):
  deq.append(itr_N+1)

i=0
while len(deq)>1:
  # 등차수열 셋팅
  i = i+K
  # 순환스캔 셋팅
  if i > len(deq):
    i = i % len(deq)
    # 0일때 예외조건 셋팅
    if i == 0:
      i = i + len(deq)
  i = i -1
  print(str(deq.pop(i)), end=", ")
# 출력
print("%s>" % str(deq.pop()))
