# https://www.acmicpc.net/problem/9020
# 1번 풀이의 한계는 매 숫자마다 소수를 찾는다는거다.
# 예를 들어 [10, 16, 8] 이라는 배열이 주어지면
# 10의 소수를 찾아. 그럼 2,3,5,7 나오겠지?
# 그리고 16의 소수를 또 찾아. 그럼 2,3,5,7,11,13가 나오겠지?
# 여기서 2, 3, 5, 7은 왜 2번 찾아? 
# 저 배열 중 가장 큰 숫자를 기준으로 한번만 소수를 찾고 그 소수를 배열에 넣은 다음 찾아쓰면 되는데?
# 예를들어 16으로 한번 소수를 다 찾아 놓고 그 배열을 A라하면 10의 소수는 A중 10보다 작은 놈들이겠지.

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