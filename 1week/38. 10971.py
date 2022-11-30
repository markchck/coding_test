# https://www.acmicpc.net/problem/10971

# 실패
import sys
input = sys.stdin.readline
N = int(input())

list_l=[]
for _ in range(N):
    list_l.append(list(map(int, input().split())))

sum = 0
for cities in list_l:
    for i in range(cities):
        sum += cities[i]

print(list_l)