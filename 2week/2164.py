import sys
input = sys.stdin.readline
from collections import deque
que = deque()

N = int(input())

for i in range(1,N+1):
    que.append(i)
# print(que)

while (len(que) != 1):
    que.popleft()
    second=que.popleft()
    que.append(second)
print(que[0])

