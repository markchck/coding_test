# 10 50 60 70 20 30 40 50
# 1  2  3  4  4  5  6  7
# 1  2  3  4  2  3  4  5

import sys
input = sys.stdin.readline
N = int(input())
items = [0] + list(map(int, input().split()))
dp = [0]*(N+1)
# mx = 0
for i in range(1, N+1):
    mx = 0
    for j in range(0, i):
        if items[i] > items[j]:
            mx = max(mx, dp[j])

    dp[i] = mx + 1
print(max(dp))


# import sys
# input = sys.stdin.readline
# N = int(input())
# items = [0] + list(map(int, input().split()))
# # print(items) [0, 10, 20, 10, 30, 20, 50]
# dp = [0]*(N+1)
# standard = 0
# for i in range(1, N+1):
#     if items[i] > standard:
#         standard = items[i]
#         dp[i] = dp[i-1] + 1
#     else:
#         dp[i] = dp[i-1]
# print(dp)
# print(dp[N])
