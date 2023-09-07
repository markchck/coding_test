# https://www.acmicpc.net/problem/15649
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sys.setrecursionlimit(10**5)


def recursion(i):
    for j in range(1, N+1):
        items.append(i)
        if j != i:
            items.append(j)
            if len(items) == M:
                return print(items)
            recursion(j)


answer = []
items = []
for i in range(1, N+1):
    recursion(i)
