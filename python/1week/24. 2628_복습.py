
w,h = map(int, input().split())
n = int(input())
width = [0, w]
height = [0, h]
 
for _ in range(n):
    a,b = map(int, input().split())
    # 가로로 자르는 경우
    if a == 0:
        height.append(b)
    # 세로로 자르는 경우
    elif a == 1:
        width.append(b)
 
width.sort()
height.sort()
 
# result = 0
# # 1. 이부분 달달 외워야겠다.. 
# # 마디별로 계산 로직이라고 부르자
# # x,y에 첫 마디 넣고 넓이 계산하고, 두 번째 마디 넣고 계산하고, 세 번째 마디 넣고 계산하고
# for i in range(len(width)-1):
#     for j in range(len(height)-1):
#         x = width[i+1] - width[i]
#         y = height[j+1] - height[j]
#         # 2. 강한자만 살아남게 하기 (굳이 배열 안쓰고 최댓값 추출 가능)
#         result = max(result, x*y)
# print(result)

# 강한자만 살아남기 로직 안 쓰고 배열하나 만들어서 푸는 풀이
result = []
for i in range(len(width)-1):
  for j in range(len(height)-1):
    x = width[i+1] -width[i]
    y = height[j+1] -height[j]
    result.append(x*y)
print(result)