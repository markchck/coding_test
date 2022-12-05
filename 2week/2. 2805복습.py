N, M = map(int, (input().split()))
A_list = list(map(int, (input().split())))

A_list.sort()
left, right = A_list[0], A_list[len(A_list)-1]

# sum = 0
# for A in A_list:
#   mid = (left+right)//2
#   if A > mid:
#     sum += (A-mid)

# if sum == M:
#   print(mid)
# elif (sum > M):
#   left = mid+1
# else:
#   right = mid-1

sum = 0
while (left <= right):
  for A in A_list:
    mid = (left+right)//2
    if A > mid:
      sum += (A-mid)
      
  if sum == M:
    print(mid)
  elif (sum > M):
    left = mid+1
  else:
    right = mid-1
