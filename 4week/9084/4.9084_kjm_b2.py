# 1차원 배열로 dp구성
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  coins = list(map(int, input().split()))
  M = int(input())

  dp = [0] * (M+1)
  dp[0]=1  #0원을 만드는 방법은 동전을 안내면 0원이니까 어떤 화폐 단위이든 0을 만드는 방법은 한가지 존재함.

  for coin in coins:
    for i in range(1,M+1):
      if i >= coin:
        dp[i] = dp[i] + dp[i-coin] 
        # 만들고자하는 i가 5인데 coin이 4이면
        # 4를 일단 쓸때라면 dp[i-coin]로 나머지 1원만 어케든 잘 만들어주면 되고 -> dp[1]
        # 4를 안 쓰는 경우라면 dp[i]로 어케든 4를 잘 만들어주면 되고 -> dp[4] 
        # 둘을 더한게 dp[4]자리에 들어가면 된다.
  print(dp[M])