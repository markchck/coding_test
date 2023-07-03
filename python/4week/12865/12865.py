import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [(0, 0)]
for _ in range(1, N+1):
    W, V = map(int, input().split())
    items.append((W, V))
# print(items)
dp = [[0] * (K+1) for _ in range(N+1)]

for n in range(1, N+1):
    for k in range(1, K+1):
        if k >= items[n][0]:
            dp[n][k] = max(dp[n-1][k], dp[n-1][k-items[n][0]] + items[n][1])
        else:
            dp[n][k] = dp[n-1][k]
print(dp[N][K])
