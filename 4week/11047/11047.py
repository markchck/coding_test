# https://www.acmicpc.net/problem/11047

# import sys
# input = sys.stdin.readline
# N,K = map(int, input().split())
# list_a = []
# for i in range(N):
#     coin = int(input())
#     if K >= coin:
#         list_a.append(coin)
# list_a.sort(reverse=True)

# count = 0
# for i in range(len(list_a)):
#     if K >= list_a[i]:
#         count =count + K // list_a[i]
#         K = K - (K//list_a[i])*list_a[i]
# print(count)



##이렇게 풀고 있으면 뭔가 잘못 됐다고 생각하고 멈추거나 다른 방향으로 생각해야할 듯..이렇게 빡구현일리가..게다가 틀림
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
list_a = [int(input()) for _ in range(N)]
count = 0
while K!=0:
    for i in range(N):
        if list_a[i] <= K: #K보다 작은 수라면?
            if len(list_a) <= (i+1): #i+1하면 인덱스 에러가 나는 경우라면?
                count += (K // list_a[i])
                K = K - ((K // list_a[i]) * list_a[i])
            else: #i+1로 다음 배열봐도 괜찮은 경우
                if list_a[i+1]<=K: #i+1번째가 K보다 작거나 같은경우 다음 번째 한번 더 봐야함
                    continue
                else: #i+1번째가 K보다 더 큰 경우 (i번째가 K를 넘지 않으면 가장 큰 숫자(그리디한 숫자에 해당))
                    count += (K // list_a[i])
                    K = K - ((K // list_a[i]) * list_a[i])
                    N = i
print(count)