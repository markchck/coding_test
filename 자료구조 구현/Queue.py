# 10845

import sys
input = sys.stdin.readline
N = int(input())
que = []
for _ in range(N):
    chunk = input().split()
    order = chunk[0]
    if (len(chunk) == 2):
        number = int(chunk[1])
        if (order == "push"):
            que.append(number)
    else:
        if (order == "pop"):
            if (que):
                print(que[0])
                que = que[1:]
            else:
                print(-1)
        if (order == "size"):
            print(len(que))
        if (order == "empty"):
            if (que):
                print(0)
            else:
                print(1)
        if (order == "front"):
            if (que):
                print(que[0])
            else:
                print(-1)
        if (order == "back"):
            if (que):
                print(que[-1])
            else:
                print(-1)
