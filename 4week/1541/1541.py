# # -나오면 다음 -가 나올 때까지 괄호로 더해나가다가 다음 -를 보면 괄호를 닫는다. 그리고 새로 시작
# import sys
# input = sys.stdin.readline
# list_a = input().strip().split('-')
# sum = 0

# list_plus = list_a[0].split('+')
# for itr in list_plus:
#     sum+=int(itr)

# for i in range(1,len(list_a)):
#     list_minus = list_a[i].split('+')
#     for itr in list_minus:
#         sum-=int(itr)
# print(sum)

import sys
input = sys.stdin.readline
list_a = input().rstrip().split('-')
ans = 0
for i in range(len(list_a)):
    if i==0:
        ans+=sum(map(int, list_a[i].split('+')))
    else:
        ans-=sum(map(int, list_a[i].split('+')))
print(ans)
            
        