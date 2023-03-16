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
        # 4를 안 쓰는 경우라면 dp[i]로 어케든 5를 잘 만들어주면 되고 -> dp[5] 
        # 둘을 더한게 dp[5]자리에 들어가면 된다.

        # dp[i] + dp[i-coin]여기에서 dp[i]는 왜 있는거냐? 싶을 수 있는데
        # dp[10]은 coin이 5일 때 한번 방문하고 coin이 7일때도 방문해서 총 2번 방문한다.
        # coin이 5일때 dp[10] = dp[10](== 0) + dp[5](==1)이라서 1인데
        # 만약 dp[i] = dp[i] + dp[i-coin] 에서 dp[i]가 없이 dp[i-coin]만 있으면
        # coin이 7일때 dp[10] = dp[10-7]이 되어서 dp[10]은 0이 된다.
        # 아까 coin이 5일 때 10을 만들 수 있던 경우의 수가 1개 있었는데 그 정보가 사라지게 된다.
  print(dp[M])