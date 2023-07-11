def solution(sequence, k):
    # dp = [0] * len(sequence)
    # dp[0] = sequence[0]
    # for i in range(1, len(sequence)):
    #     dp[i] = dp[i-1] + sequence[i]
    answer = []
    len_s = len(sequence)
    dp = [[0]*(len_s) for _ in (range(len_s))]
    for i in range(len_s):
        for j in range(i, len_s):
            if (i == j):
                dp[i][j] = sequence[j]
                if dp[i][j] > k:
                    break
                if (dp[i][j]) == k:
                    answer.append([i, j, j-i])
            else:
                dp[i][j] = dp[i][j-1] + sequence[j]
                if dp[i][j] > k:
                    break
                if (dp[i][j]) == k:
                    answer.append([i, j, j-i])
    answer.sort(key=lambda x: (x[2], x[0], x[1]))
    return [answer[0][0], answer[0][1]]


solution([1, 2, 3, 4, 5], 7)
