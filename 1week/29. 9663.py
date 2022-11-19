# 파이파이로 제출해야 통과

import sys

N = int(sys.stdin.readline())
queen = [0] * N
result = 0

def check(x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == x - i:
            return False
    return True

def dfs(x):
    global result

    if x == N:
        result += 1
    else:
        for i in range(N):
            queen[x] = i
            if check(x):
                dfs(x+1)

dfs(0)
print(result)
