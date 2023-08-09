# 괄호를 어떻게 그리던 결국 최종적으로 행렬 A와 행렬 B가 남을 것이다.
# 정답은 A가 나오는데 걸린 연산 수 + B가 나오는데 걸리는 연산 수 + A와 B를 곱하는데 걸리는 연산 수가 될 것이다.
# A가 나오는데 걸린 연산 수도 최종적으로 어떤 행렬 두개가 나오는데 걸린 연산수 + 두 행렬을 곱하는데 걸리는 연산수가 된다. (재귀적이고, DP에 넣은걸 활용하면 될 듯)

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
dp = [[0 for _ in range(N)] for _ in range(N)]


for i in range(1, N):  # 몇 번째 대각선?
    for j in range(0, N-i):  # 대각선에서 몇 번째 열?

        if i == 1:  # 차이가 1밖에 나지 않는 칸
            dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue

        dp[j][j+i] = 2**32  # 최댓값을 미리 넣어줌
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i],
                             dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])


print(dp[0][N-1])  # 맨 오른쪽 위
