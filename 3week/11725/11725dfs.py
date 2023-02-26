import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N =int(input())
nodes = [[] for _ in range(N+1)]
parents = [0] * (N+1)

for i in range(N-1):
    a,b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
print(nodes)
def dfs(x):
    for itr in nodes[x]:
        if parents[itr] == 0:
            parents[itr] = x
            dfs(itr)
        else:
            continue
dfs(1)

for i in range(2, len(parents)):
   print(parents[i])

