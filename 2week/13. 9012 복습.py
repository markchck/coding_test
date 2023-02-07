import sys
input = sys.stdin.readline

from collections import deque

que = deque()
N=int(input())
for _ in range(N):
    A = (input().split())
    # 이거 어케하면 될 것 같냐면 길이만큼 반복문 돌면서 짝이 맞으면 pop해서 없애고 안 맞으면 False 전부다 pop되어서 없어지면 true
    if (A[0] == A[-1]):
        print("NO")
    else:
        print("YES")

# print(que)
