# https://www.acmicpc.net/problem/2637
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
nodes= [[] for _ in range(N+1)]
for i in range(M):
    X, Y, K = map(int, input().split())
    nodes[X].append([Y, K])
for i in range(N+1):
    if nodes[i]:
        middle_part_start= i
        break

def dfs(x): #6
    for itr in nodes[x]: #[5, 2], [3, 3], [4, 4]
       print(itr)

for itr in nodes:
    if itr: #itr = [[1,2], [2,2]]
        for itr2 in itr: #itr2 = [1,2]
            if itr2[0] >=middle_part_start:
                dfs(itr2[0]) #6 같이 중간부품 쪼개기 들어감
    
   
    # 중간부품이 보이면 dfs로 기본부품으로 바꾸고
    # 마지막에 N번째노드의 기본 부품들을 전부 출력한다.