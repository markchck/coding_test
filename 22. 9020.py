# https://www.acmicpc.net/problem/9020
# 1. 소수를 구하는 함수를 만든다
# 2.10이 주어지면 10보다 작은 소수를 모두 구하고
# 3 그 소수들 중 하나씩  
#     3.1 그 소수를 2번 더해서 10이 나오나 확인하고 나오면 그 놈이 골디바흐
#     3.2 (아니라면) 그 소수를 10과 빼고 나머지 값이 다른 소수리스트에 잇는지 확인한다. 그놈이 골디바흐임.

Times = int(input())
for t in range(Times):
  number = int(input())
  # select_p_number(number)

# number(ex. 10)보다 작은 소수들을 배열로 뱉는 함수를 만들 것.
def select_p_number(number):
  if number==1:
    None
  elif number ==2:
    return number
  elif number
  for n in range(2, number):
    n
