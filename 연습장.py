import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
nodes = [[] for _ in range(N+1)]
parents = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

que =deque()
def bfs(x):
    parents[x]=x
    que.append(x)
    while que:
        num=que.popleft()
        for itr in nodes[num]:
            if parents[itr] == 0:
                parents[itr] = num
                que.append(itr)
bfs(1)

for i in range(2, N+1):
    print(parents[i])