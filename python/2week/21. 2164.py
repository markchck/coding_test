# https://www.acmicpc.net/problem/2164
import sys
from collections import deque

deq=deque()

N=int(sys.stdin.readline().strip())
for i in range(N):
    deq.appendleft(i+1)

for i in range(len(deq)):
    if len(deq) > 1:
        deq.pop()
        deq.appendleft(deq.pop())
print(deq[0])
        
