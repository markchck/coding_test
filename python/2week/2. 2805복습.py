import sys
N,M = map(int, sys.stdin.readline().split())
trees=list(map(int, sys.stdin.readline().split()))

min = 0
max = max(trees)

def cutting(min, max):
  while ((min <= max)):
    mid = (min+max)//2
    sum = 0

    for tree in trees:
      if (tree>mid):
        sum = sum + (tree - mid)
    
    #sum>M일때 min을 올리는건 당연하고,,sum == M이어도 한번 더 min을 올려봐서 나무를 덜 잘르면서 최소 M을 만족하는지 확인해야함.
    if (sum >= M): 
      min = mid+1
    else:
      max = mid-1
  print(max)

cutting(min, max)






# N, M = map(int, (input().split()))
# A_list = list(map(int, (input().split())))

# A_list.sort()
# left, right = A_list[0], A_list[len(A_list)-1]

# # sum = 0
# # for A in A_list:
# #   mid = (left+right)//2
# #   if A > mid:
# #     sum += (A-mid)

# # if sum == M:
# #   print(mid)
# # elif (sum > M):
# #   left = mid+1
# # else:
# #   right = mid-1

# sum = 0
# while (left <= right):
#   for A in A_list:
#     mid = (left+right)//2
#     if A > mid:
#       sum += (A-mid)
      
#   if sum == M:
#     print(mid)
#   elif (sum > M):
#     left = mid+1
#   else:
#     right = mid-1
