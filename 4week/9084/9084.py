# import sys
# input = sys.stdin.readline



# T = int(input())
# for  _ in range(T):
#     N = int(input()) #동전개수
#     coins = map(int, input().split()) # 동전들
#     M = int(input()) #만들어야하는 금액
    
#     dp = [0] * (M+1)
#     dp[0]=1

#     for coin in coins:
#         for i in range(1,M+1):
#             if i>=coin:
#                 dp[i] = dp[i] + dp[i-coin]
#     print(dp[M])

import sys
sys.setrecursionlimit(100000000)


def make_money(coin, money):
    if money == 0:
        return 1
    
    if money < 0 or not coin:
        return 0
    
    # 5와 7로 10을 만드는 경우의 숫자는
    # 7을 안쓰고 10 만들어봐 + 7을 쓰고 만들어봐를 더하면 된다.
    return make_money(coin[:-1], money) + make_money(coin, money - coin[-1])

test_count = int(input())

coin_count = [0] * test_count
coins = []
price = [0] * test_count

for i in range(test_count):
    coin_count[i] = int(input())
    coins.append(list(map(int, input().split())))
    price[i] = int(input())

for i in range(test_count):
    print(make_money(coins[i], price[i]))
