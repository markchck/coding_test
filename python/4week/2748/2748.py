## set로 메모이제이션 하고 재귀 사용 (재귀로 메모이제이션 하는게 반복문보다 더 활용도가 좋을 듯)
N =int(input())
memo = {0:0,1:1}

def fib(n):
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
print(fib(N))


# set말고 list로 메모이제이션 하고 재귀로 돌고
N = int(input())
memo = [-1]*(N+1)
memo[0] = 0
memo[1] = 1

def pibonachi(n):
    if memo[n] !=-1:
        return memo[n]
    memo[n] = pibonachi(n-1)+pibonachi(n-2)
    return memo[n]
print(pibonachi(N))

## 리스트로 메모이제이션 하고 반복문으로 (떠올리기 쉽지 않을듯)
# import sys
# input = sys.stdin.readline
# N = int(input())
# dp = [0]*(N+1)
# dp[1] = 1

# for i in range(2, N+1):
#     dp[i] = dp[i-1] + dp[i-2]

# print(dp[N])


# import sys
# input = sys.stdin.readline
# N = int(input())
# def pibonachi(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (pibonachi(n-1) + pibonachi(n-2))

# print(pibonachi(N))