import sys
from collections import deque
input = sys.stdin.readline
N, M, K ,X = map(int, input().split())

nodes = [[] for _ in range(N+1)]
count = [0] * (N+1)
visit = [0] * (N+1)
result =[]
que = deque()

for _ in range(M):
    a, b = map(int, input().split())
    nodes[a].append(b)

def bfs(x):
    visit[x]=1
    que.append(x)
    while que:
        x=que.popleft()
        for itr in nodes[x]:
            if visit[itr] == 0:
                visit[itr] = 1
                count[itr]= count[x]+1
                if count[itr] == K:
                    result.append(itr)
                else:
                    que.append(itr)

bfs(X)

if result:
    A = sorted(result)
    print(*A)
else:
    print(-1)





# def dfs(x):
#     global count
#     visit[x] = 1
#     for itr in nodes[x]:
#         if visit[itr] == 0:
#             visit[itr] = 1
#             count[itr]+=1
#             if count[itr] ==K:
#                 result.append(itr)
#             else:
#                 dfs(itr)
# dfs(X)
# print(result)




#dfs

# import sys
# input = sys.stdin.readline
# N, M, K ,X = map(int, input().split())
# nodes = [[] for _ in range(N+1)]
# count = [0] * (N+1)
# visit = [0] * (N+1)
# # count = 0
# result =[]

# for _ in range(M):
#     a, b = map(int, input().split())
#     nodes[a].append(b)

# def dfs(x):
#     global count
#     visit[x] = 1
#     for itr in nodes[x]:
#         if visit[itr] == 0:
#             visit[itr] = 1
#             count[itr]+=1
#             if count[itr] ==K:
#                 result.append(itr)
#             else:
#                 dfs(itr)
# dfs(X)
# print(result)