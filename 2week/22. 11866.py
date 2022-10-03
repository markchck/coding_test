# https://www.acmicpc.net/problem/11866
# 9시 14분 시작

from collections import deque
import sys

N, K=map(int, (sys.stdin.readline().split(" ")))

deq = deque()
for itr_N in range(N):
  deq.append(itr_N+1)

