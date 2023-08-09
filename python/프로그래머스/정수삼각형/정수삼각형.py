import sys


def solution(triangle):
    # 이전까지 간 최대값을 기록해놨다가 재사용하면 되니 dp에 해당
    N = len(triangle)
    dp = []
    for i in range(N):
        dp.append([-sys.maxsize]*(i+1))
    dp[0] = triangle[0]
    for i in range(1, N):
        M = len(dp[i])
        for j in range(M):
            if j == 0:  # 왼쪽 부모가 없는 경우
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == M-1:  # 오른쪽 부모가 없는 경우
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:  # 양쪽 부모 둘 다 있는 경우
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[N-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
