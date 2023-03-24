#사이클이 생기면 NO를 출력해보자.
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())

def dfs(x):
    global flag
    if result[x] == 0:
        result[x]=1
    
    for itr in list_a[x]:
        if result[itr] == 0:
            result[itr] = -1 * result[x]
            dfs(itr)
        elif result[itr] == result[x]:
            flag = 0

for _ in range(N):
    V,E = map(int, input().split())
    list_a = [[] for _ in range(V+1)]
    result = [0]*(V+1)
    for _ in range(E):
        u,v = map(int, input().split())
        list_a[u].append(v)
        list_a[v].append(u)
    flag = 1

    # 전체 노드를 탐색하지 않고 dfs(1)만 하는 경우 반례 
    # 1
    # 5 4
    # 1 2
    # 3 4
    # 4 5
    # 3 5
    # 두개의 영역으로 분리 되어있고 한 영역은 이분그래프를 만족하고 다른 영역은 만족하지 않는 경우 dfs(1)만 보고 YES라고 한다.
    for i in range(1,V+1):
        dfs(i)
    # dfs(1)

    print("YES" if flag==1 else "NO")