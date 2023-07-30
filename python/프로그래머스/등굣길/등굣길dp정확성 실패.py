def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    for r in range(1, n+1):
        for c in range(1, m+1):
            if [c, r] in puddles:
                dp[r][c] = 0
                continue
            if r == 1 and c == 1:
                dp[1][1] = 0
                continue

            if ([c, r-1] in puddles and [c-1, r] not in puddles) or ([c, r-1] not in puddles and [c-1, r] in puddles):
                dp[r][c] = dp[r-1][c-1] + 1
                continue

            dp[r][c] = dp[r-1][c-1]+2
    return (dp[n][m])


solution(4, 3, [[2, 2]])
