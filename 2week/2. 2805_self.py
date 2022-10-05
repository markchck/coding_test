# 이거 시간초과 뜰텐데 
import sys
# N, M = map(int, input().split(" "))
N,M = map(int, sys.stdin.readline().split(" "))
# trees = list(map(int, input().split(" ")))
trees = list(map(int, sys.stdin.readline().split(" ")))

min = 0
max = max(trees)
# 1부터 하나씩 늘려가며 모든 h값을 조회하면 개느리니 이진탐색 고고

def cutting(min,max):
  while min <=max:
    mid = (min+max)//2
    sum = 0
    for tree in trees:
      if (tree>mid):
        sum = sum + tree-mid
      # else: #이부분 때문에 시간초과 뜸. (굳이 없어도 되는 else를 한번 더 갔다가 오니까)
      #   pass

    if (sum>=M): #너무 낮게 height를 설정함.
      min = mid+1
    elif(sum<M):
      max = mid-1
  print(max) 
cutting(min,max)

  # if(sum==M):   #내가짠 코드는 이 밑인데 반례줄게 N=2, M=2 나무크기 3, 2 //이래도 mid가 2이고 3과 1도 mid가 2? 
  #   break
  # elif(sum>M):
  #   min = mid+1
  # else:
  #   max = mid-1

# print(mid)
  

