# https://www.acmicpc.net/problem/11047
# 매순간 최적의 선택을 해야하는 그리디 상황임.
# 그리디 문제의 핵심은 최적의 상태를 만드려면 무슨 기준으로 뽑을 건지 정하는 것이다.
# 이 문제에서는 단위가 큰 동전이라는 직관적인 감이 있지만 어떤 문제는 빨간색 동전일수도 있고, 어떤 문제에서는 크기가 큰 동전이 좋은 것일수도 있다.
# 문제 상황마다 '이렇게 하면 최적의 상황이 되겠다'는 가설을 세우는게 핵심임!
import sys
from collections import deque
deq = deque()
input = sys.stdin.readline
N,K = map(int, input().split())

for i in range(N):
    deq.appendleft(int(input()))
# print(deq)

count=0
for coin in deq:
    if K >0:
        if coin > K:
            continue
        else:
            tmp_value= (K//coin)
            K = K - coin*tmp_value
            count= count + tmp_value
print(count)


# 재현이 코드 리뷰
# import sys
# N, K = map(int, sys.stdin.readline().split())
# money = []
# for _ in range(N):
#     tmp = int(sys.stdin.readline().rstrip())
#     if tmp <= K:   # 이 부분이 좋았음. 애당초 K보다 큰 동전은 배열에 넣을 필요가 없지. K보다 작은것만 배열에 담음 
#         money.append(tmp)


# count = 0
# for i in range(len(money)-1, -1, -1):
#     count += K//money[i]
#     K -= (K//money[i])*money[i]

# sys.stdout.write(f'{count}')