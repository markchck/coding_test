# 일단 브루트포스는 시간너무걸릴거다.
  # 집의 개수가 20만이라 최악의 경우 (200,000 combination 199,999) 하면 사실상 20만 팩토리얼의 경우의 수가 생기게 된다.
  # 그 모든 상황에 공유기를 설치하면서 각 공유기간의 최대 거리를 계산할 수는 없음.

# 그럼 어카냐? (브루트포스가 어렵다면 분할하여 logN으로 쪼갤수 있는지 봐보자)
  # 여기까진 생각하겠는데.. 무엇을 반으로 나누냐..?

# https://www.acmicpc.net/submit/2110/50043187

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
A_list = [ int(input()) for _ in range(N) ]
A_list.sort()

def BOJ2110():
  max = A_list[-1] - A_list[0]
  min = 1
  count = 1

  while(min <= max):
    count =1 
    mid = (max+min)//2
    house = A_list[0]
    for i in range(1, len(A_list)):
      if A_list[i] - house >= mid:
        count +=1
        house = A_list[i]
    if count >= C:
      result = mid
      min = mid +1
    else:
      max = mid -1
  print(result)

BOJ2110()
