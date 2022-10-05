# https://www.acmicpc.net/problem/2798
# 어떻게하면 컴퓨터한테 노가다를 시킬 수 있을지...
# 컴터가 노가다는 끝내주게 잘하는데 왜 노가다를 시키질 못하니..

N, M= map(int, input().split(" "))
sorted_list_N = list(map(int, input().split(" ")))

# 1. 노가다는 시켰고 (두번째 자리는 첫째자리 +1부터~마지막 문자-1까지 올 수 있다는 사실 중요)
new_list=[]
for a in range(0, N-2):
  A = sorted_list_N[a]
  for b in range(a+1, N-1):
    B= sorted_list_N[b]
    for c in range(b+1, N):
      C=sorted_list_N[c]
      if (A+B+C)<M: #이 조건 제대로 안 읽어서 틀린거네..
        new_list.append(A+B+C)

# 2. new_list 결괏값과 M과 차이가 가장 근소한 것 찾아야함. 
order=[]
for i in range(len(new_list)):
  order.append(abs(M-new_list[i]))
min_index = order.index(min(order))

# print(new_list)
print((new_list[min_index]))



# N, M= map(int, input().split(" "))
# sorted_list_N = list(map(int, input().split(" ")))
# # sorted_list_N= sorted(list_N, reverse=True)

# # 1. 노가다는 시켰고 (두번째 자리는 첫째자리 +1부터~마지막 문자-1까지 올 수 있다는 사실 중요)
# new_list=[]
# for a in range(0, N-2):
#   A = sorted_list_N[a]
#   for b in range(a+1, N-1):
#     B= sorted_list_N[b]
#     for c in range(b+1, N):
#       C=sorted_list_N[c]
#       if (A+B+C)<M: #이 조건 제대로 안 읽어서 틀린거네..
#         new_list.append(A+B+C)
# # new_list=[]
# # for a in range(0, len(sorted_list_N)-2):
# #   if(sorted_list_N[a]>=M):  &&첫째자리에 20이 오는 경우를 피하는 알고리즘을 짤 수 없어서 브루트포스한거 아니냐는거지..
# #     pass
# #   else:
# #     A = sorted_list_N[a]
# #     for b in range(a+1, len(sorted_list_N)-1):
# #       if(sorted_list_N[b]-A>=M):
# #         pass
# #       else:
# #         B= sorted_list_N[b]
# #         for c in range(b+1, len(sorted_list_N)):
# #           if(sorted_list_N[c]-B-A>=M):
# #             pass
# #           else:
# #             C=sorted_list_N[c]
# #             new_list.append(A+B+C)

# # 2. new_list 결괏값과 M과 차이가 가장 근소한 것 찾아야함. 
# order=[]
# for i in range(len(new_list)):
#   order.append(abs(M-new_list[i]))
# min_index = order.index(min(order))

# print(new_list)
# print(new_list[min_index])



# while문으로 a,b,c들 바꿔가면서 할랬는데 설정값 주기 극악 난이도였음. for문이 몇 번 반복할지 판단하는 경우에는 더 쉽네.
# A=0
# B=0
# C=0

# a=0
# b=0
# c=0

# l=len(sorted_list_N)

# list=[]
# while a<(l-2):
#   A=sorted_list_N[a] #9
#   b=b+1
#   while b<(1:l-1):
#     B=sorted_list_N[b] #8

#     while c<l:
#       C=sorted_list_N[c]
#       list.append(A+B+C)
 
#     b=b+1
#     a=a+1
#     c=b+1
