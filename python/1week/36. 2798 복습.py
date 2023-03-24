# 이 문제가 왜 완전탐색인지를 이해하려면 콤비네이션이 아니라 삼중포문으로 풀어야함.
N,M = map(int, input().split())
card_num = list(map(int, input().split()))

result = 0
a=0
for i in range(N):
  for j in range(i+1, N):
    for z in range(j+1, N):
      card_combi_sum = card_num[i] + card_num[j] + card_num[z]
      if card_combi_sum <= M:
        result = max(result, card_combi_sum)
        # print(a)
        print(result)

print(result)



