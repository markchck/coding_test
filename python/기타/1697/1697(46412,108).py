from collections import defaultdict
import sys
dp = defaultdict(lambda: sys.maxsize)


input = sys.stdin.readline

N, K = map(int, input().split())
dp[N] = 0


def solution(N, K):
    for i in range(N):
        dp[i] = N-i

    for i in range(0, K+1):
        if (2*i <= K):
            dp[2*i] = min(dp[2*i], dp[i]+1, dp[2*i-1]+1, dp[2*i+1]+1)
        else:
            dp[2*i] = min(dp[2*i], dp[i]+2, dp[2*i-1]+1,  dp[2*i+1]+1)

        if (i+1 <= K):
            dp[i+1] = min(dp[i+1], dp[i]+1)
        else:
            dp[i+1] = min(dp[i+1], dp[i]+1)

        if (i-1 <= K):
            dp[i-1] = min(dp[i-1], dp[i-2]+1, dp[i]+1)
        else:
            dp[i-1] = min(dp[i-1], dp[i-2]+1, dp[i]+1)

    return dp[K]


print(solution(N, K))
