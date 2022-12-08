# 일단 브루트포스는 시간너무걸릴거다.
  # 집의 개수가 20만이라 최악의 경우 (200,000 combination 199,999) 하면 사실상 20만 팩토리얼의 경우의 수가 생기게 된다.
  # 그 모든 상황에 공유기를 설치하면서 각 공유기간의 최대 거리를 계산할 수는 없음.

# 그럼 어카냐? (브루트포스가 어렵다면 분할하여 logN으로 쪼갤수 있는지 봐보자)
  # 여기까진 생각하겠는데.. 무엇을 반으로 나누냐..?

# https://www.acmicpc.net/submit/2110/50043187

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
A_list = []
for _ in range(n):
  A_list.append(int(input()))

A_list.sort()

max = A_list[-1] - A_list[0]
min = 1

while not (min > max):
  count =1
  recent_house = A_list[0]
  mid = (min+max)//2
  for i in range(1, len(A_list)):
    if A_list[i] - recent_house >= mid:
      count +=1
      recent_house = A_list[i]

  if count >= c:
    result = mid
    min = mid +1
  else:
    max = mid -1
print(result)