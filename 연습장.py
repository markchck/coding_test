def solution(triangle):
    row = len(triangle)
    dp = []
    # for i in range(row):
    #     col = len(triangle[i])
    #     for j in range(col):
    #         dp.append([0] * (col))
    # print(dp)
    for i in range(row):
        col = len(triangle[i])
        dp.append([-99999999999999] * (col))

    dp[0][0] = triangle[0][0]

    for i in range(1, row):
        col = len(triangle[i])
        for j in range(col):
            if j == 0:  # 맨 왼쪽
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j+1 == col:  # 맨 오른쪽
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:  # 중간
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    return max(dp[row-1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
