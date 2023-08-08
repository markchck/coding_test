# 최소 스패닝 트리 = 크루스칼 또는 프림 알고리즘
# 그리디하게 뽑기 위해 가중치를 작은순으로 정렬하고, 뽑을 때마다 싸이클이 생기는지 확인(부모가 같은지 확인)해서
# 생기면 패스하고 안생기면 연결하는 작업(부모를 작은 숫자 기준으로 바꾸는 작업)

import sys
input = sys.stdin.readline
V, E = map(int, input().split())

parents = []
for i in range(V+1):
    parents.append(i)
# print(parents) # [0, 1, 2, 3]

nodes = []
for i in range(E):
    A, B, C = map(int, input().split())
    nodes.append((C, A, B))

nodes.sort(key=lambda x: x[0])


def find_parent(i):
    if i == parents[i]:
        return i
    else:
        return find_parent(parents[i])


def union(s, e):
    s = find_parent(s)
    e = find_parent(e)
    if s > e:
        parents[s] = e
    else:
        parents[e] = s


answer = 0
for node in nodes:
    cost, start, end = node
    sParent = find_parent(start)
    eParent = find_parent(end)
    if sParent != eParent:
        union(start, end)
        answer += cost
print(answer)
