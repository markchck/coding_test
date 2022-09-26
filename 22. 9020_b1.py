# https://www.acmicpc.net/problem/9020
# 1. 소수를 구하는 함수를 만든다 0
# 2. 10이 주어지면 10보다 작은 소수를 모두 구하고 0
# 3. 그 소수들 중 하나씩  
#     3.1 그 소수를 2번 더해서 10이 나오나 확인하고 나오면 그 놈이 골디바흐
#     3.2 (아니라면) 그 소수를 10과 빼고 나머지 값이 다른 소수리스트에 잇는지 확인한다. 그놈이 골디바흐임.
# 4. 출력될 때 3,7만 출력되고 7,3은 안되게 하는 코드
# 5. 소수의 차이가 덜 나는 걸 먼저 뽑아내는 코드

# 이대로 내면 시간 초과가 뜸! (효율화 할 수 있는 부분 찾아야함.)


# 1. 소수를 구하는 함수를 만든다 0
# number(ex. 10)보다 작은 소수들을 배열로 뱉는 함수를 만들 것.
def return_p_number_list(number): #문제조건 상 number>2
  prime_number_list = []
  for n in range(2, number):
    error = 0
    # n이 소수인지 판별해야함.
    if n ==2:
      prime_number_list.append(n)
    elif n%2==0:
      None
    else:
      # n까지 소수가 몇개 있는지 판별
      for itr_n in range(2, n):
        if itr_n==2:
          prime_number_list.append(n)
        elif itr_n%2 ==0:
          error = error +1
        else:
          if n%itr_n == 0:
            error = error+ 1
      if error ==0:
        # n이 다 돌 때까지 전부다 나머지가 0이여야 소수인거임. 중간에 하나 안 나눠졌다고 소수로 봐주면 안됨
        prime_number_list.append(n)

  out_put_list=[]
  for prime_number in prime_number_list:
    if prime_number ==None:
      None
    else:
      out_put_list.append(prime_number)
  return out_put_list

Times = int(input())
input_list=[]
for t in range(Times):
  number = int(input())
  input_list.append(number)

output_list=[]
for itr_input_list in input_list:
  number = itr_input_list
  goldi = []
  for i in return_p_number_list(number):
    if i+i == number:
      goldi.append([i,i])
      # break
    else:
      if (number - i) in return_p_number_list(number):
        goldi.append([i, number-i])
  
  # 4
  for itr_goldi in goldi:
    if (itr_goldi[0] > itr_goldi[1]):
      del(itr_goldi)
    elif(itr_goldi[0] == itr_goldi[1]):
        first_output = itr_goldi[0]
        second_output = itr_goldi[1]
    else:
        first_output = itr_goldi[0]
        second_output = itr_goldi[1]
  output_list.append([first_output, second_output])

for itr_output_list in output_list:
  print(itr_output_list[0], itr_output_list[1])