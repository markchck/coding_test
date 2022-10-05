# https://www.acmicpc.net/problem/2805

# 12시 46분 시작
# 1시 57분 종료. 못풀었음. (1시간 20분 투자)

# 내계획 배열들에 인덱싱(left=0, right=4)을 주고 a[left], a[right] 값을 조정해서 mid값을 구할랬는데
# 결론적으로는 인덱싱으로 이분탐색하면 안됨.
# 이렇게 풀면 안됨.
# 왜냐 targetnumber는 꼭 배열에 있는 숫자가 아니라 36처럼 배열 사이에 있는 숫자를 원하는거거든. 
# 나처럼 인덱싱을 통해 targetnumber를 구하려하면 배열안에 잇는 숫자중에서 targetnumber를 구할수밖에 없게 된다. (문제의 의도와는 다름)

N, M = map(int, input().split(" ")) #나무의 수
trees=list(map(int, input().split(" ")))
# M의 범위는 trees의 가장 왼쪽 값 이상 가장 오른쪽 값 이하 M값을 하나씩 증가시키면 느려
# h(맞출 나무길이) 범위 중 가운데 먼저 tree들에 각각 빼보고 그 값들의 합이 M보다 작으면 왼쪽, 크면 오른쪽 (이진탐색이네)

# 일단 정렬먼저
trees.sort()

left = 0
right = N-1
# # min_tree < target_h < max_tree


# # 첨엔 각각 나무들을 이터레이팅 해야하니 for라고 생각했는데
# 아니다 for로 돌리면 따박따박 1씩 강제로 증가해야하니 While로해야함. 이분탐색은+1씩 증가하는게 아니다.

while left<=right:
  mid = (left+right)//2
  min_tree_h = trees[left]
  max_tree_h = trees[right]
  mid_tree_h = (min_tree_h+max_tree_h)//2
  sum = 0

  for tree in trees:
    if (tree - mid_tree_h)>0:
      sum = sum+ (tree - mid_tree_h)
    else:
      pass

  # 웬만하면 인덱싱을 직접 입력하는 상황을 피하기위해 for in 으로 다시 시도해볼게..
  # 인덱싱을 하기 시작하면 복잡해짐.. 웬만하면 피하자.

  # # 인덱싱이 필요해서 i값 구할 수 잇는 For문 돌리겠음. (ㄴㄴ 위에 index안하고도 잘만 쓰는 중)
  # for i in range(len(trees)):
  #   if (trees[i] - mid_tree_h)>=0:
  #     sum = sum+ (trees[i] - mid_tree_h)
  #   else: #기준점보다 낮은 나무들은 고려대상 아님
  #     pass

  if sum == M:
    break
  elif(sum < M): #sum이 M보다 작다는 소리는 너무 높이 짤라서 남겨먹을게 별로 없다는 이야기
    right = mid-1
  else:
    left= mid+1 #너처럼 인덱싱을 가지고 조절하려햇으면 여기서 막힘..
    
print(trees[mid])



