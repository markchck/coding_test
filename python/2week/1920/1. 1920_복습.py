# 와..리스트와 해쉬set이 이정도로 탐색속도 차이가 난다고?
# N = int(input())
# A_list = set(map(int, input().split()))
# M = int(input())
# B_list = list(map(int, input().split()))

# for b in B_list:
#   if b in A_list:
#     print(1)
#   else:
#     print(0)

N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))

A_list.sort()

for B in B_list:
  left, right = 0, N-1
  isExist = False

  while (left <= right):
    mid = (left+right)//2
    if B == A_list[mid]:
      print(1)
      isExist = True
      break
    elif (B > A_list[mid]):
      left = mid+1
    else:
      right =mid-1
  if isExist ==False:
    print(0)

