# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# 감이 안옴...

import sys
input=sys.stdin.readline

brown, yellow = map(int, input().split())
sum = brown+yellow
# answer = []
# yellow 약수 구하기
for i in range(1, yellow+1):
    if(yellow % i) == 0:
        # i는 yellow의 절반을 넘지 않게
        # if yellow//2 >= i :
            # yellow가 24일 때 2가 i이면 big은 12임
            big = yellow//i
            # 2씩 더하는 이유는 패딩 고려
            if (i+2) * (big+2) == sum:
                print([big+2,i+2])
                break
# print(answer)



# def solution(brown, yellow):
#     sum = brown+yellow

#     answer = []
#     # yellow 약수 구하기
#     for i in range(1, yellow+1):
#         if(yellow % i) == 0:
#             # i는 yellow의 절반을 넘지 않게
#             if yellow//2 >= i :
#                 # yellow가 24일 때 2가 i이면 big은 12임
#                 big = yellow//i
#                 # 2씩 더하는 이유는 패딩 고려
#                 if (i+2) * (big+2) == sum:
#                     answer.append(i+2, big+2)
#     return answer