# 1
# 11 00 
# 100 001 000  
# 1100 1001 0000 0011 1111
# 11111 11100 11001 10011 00111 00001 00100 10000 (00000은 불가)

##통과 69788	364
import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) %15746
print(dp[N])


# import sys
# input = sys.stdin.readline
# N = int(input())
# dp = [0] * (N+2)
# size=[0]*(N+2)
# dp[1] = 1
# dp[2] = 2
# size[1] = sys.getsizeof(dp[1])
# size[2] = sys.getsizeof(dp[2])

# for i in range(3, N+1):
#     dp[i] = (dp[i-1] + dp[i-2])
#     size[i] = sys.getsizeof(dp[i])

# print(dp[N])
# print(size[N])

##메모리초과
# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline
# N = int(input())
# memo = {1:1, 2:2}
# def boj1904(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = (boj1904(n-2)+boj1904(n-1)) % 15746
#         return memo[n]
# print(boj1904(N))

## 변수 2개만으로 풀어보고, 15746으로 나눠야하는 이유, 재귀로 풀어서 메모리 초과 뜬 이유, indexError런타임에러 뜬 이유 적기
import sys
input = sys.stdin.readline
N = int(input())
a=1
b=1
for i in range(N-1): #4번
    a,b = b%15746, (a+b)%15746
print(b)