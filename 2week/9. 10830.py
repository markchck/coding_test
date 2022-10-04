# https://www.acmicpc.net/problem/10830

import sys
N, B = map(int, sys.stdin.readline().split())
list=[]

# N*N입력 받는거 어케하더라..
for i in range(N):
    list.append(list(map(int, sys.stdin.readline().split())))


# def main(B):
#   if B ==1:
#     return list
#   else:
#     return main(B-1) * list

# main(B)