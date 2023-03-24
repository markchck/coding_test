# https://www.acmicpc.net/problem/9020
# 1번 풀이의 한계는 매 숫자마다 소수를 찾는다는거다.
# 예를 들어 [10, 16, 8] 이라는 배열이 주어지면
# 10의 소수를 찾아. 그럼 2,3,5,7 나오겠지?
# 그리고 16의 소수를 또 찾아. 그럼 2,3,5,7,11,13가 나오겠지?
# 여기서 2, 3, 5, 7은 왜 2번 찾아? 
# 저 배열 중 가장 큰 숫자를 기준으로 한번만 소수를 찾고 그 소수를 배열에 넣은 다음 찾아쓰면 되는데?
# 예를들어 16으로 한번 소수를 다 찾아 놓고 그 배열을 A라하면 10의 소수는 A중 10보다 작은 놈들이겠지.

# 입력된 숫자들 중 가장 큰 수를 찾는 로직 (0)
# 그 숫자까지의 소수를 찾고 새로운 배열 A를 만드는 로직 (8이면 2 3 5 7) (0)
# 다른 넘버의 소수도 A를 보고 찾는 로직 (0)
# 골디바흐의 수 찾는 로직
  # 두번 연속으로 더해서 10이나오면 그놈을 출력하고 (ex. 5+5)
  # 그런 값이 없으면 3+7출력 하는데 둘 차이가 제일 적은놈 추출 (이게 생각보다 어렵네?)

# 시간초과 뜸.
# 내 코드의 문제 
  # 1. 소수 판별 코드 복잡 (인터넷 찾아보면 훨씬 더 간단하게 할 수 있네)
  # 2. 소수 판별 시간 복잡도 Big(n)임. n개의 숫자가 주어지면 n개*n-1개 조회해야하니 Big(n^2)임
  # 3. 리스트에 한번에 넣어놓는건 1번풀이보다 아이디어가 좋긴 했는데. 리스트를 조회하는 시간도 걸리긴함.
  # 4. 차이가 가장 적은 놈을 추출하는 코드도 예를들어 16가 들어왔다면 8,8부터 나눠서 소수인지 검사하고 맞으면 print
      #  아니면 앞에 자리는 -1, 뒤에자리는 +1해서 7,9로 만들고 소수만으로 이루어져 있는지 검사. 계속 반복해서 5, 11이 되면 print 

def return_p_number_list(max_value):
  prime_number_list = []
  for value in range(2, max_value):
    if value == 2:
      prime_number_list.append(value)
    elif value % 2 == 0:
      pass
    else:
      # 9이 소수인지 판단하려면 3미만의 숫자로 3을 나눴을 때 나머지가 0이되는 숫자가 있는지 체크 -> 없으면 소수
      error = 0
      for itr_value in range(2, value): #value = 9
        if value%itr_value == 0:
          error = error+1
          break
      if error == 0:
        prime_number_list.append(value)
  return prime_number_list

def quick_serarch(value, prime_number_list):
  return_quick_search_list =[]
  for i in range(len(prime_number_list)):
    if prime_number_list[i] <= value: #value는 퀵서치할 숫자 ex. 6
      return_quick_search_list.append(prime_number_list[i])
  return return_quick_search_list

Times = int(input())

input_list = []
for t in range(Times):
  number = int(input())
  input_list.append(number)

# 최대값의 소수를 찾는 로직
max_value  = max(input_list)
prime_number_list = return_p_number_list(max_value)

# 이미 찾아진 소수를 활용해서 다른 숫자들의 소수를 찾는 로직
for itr_input_list in input_list:
  quick_prime_list = quick_serarch(itr_input_list, prime_number_list)
  golid = []
  for itr_quick_prime in quick_prime_list:
    if (itr_quick_prime*2 == itr_input_list):
      golid.append([itr_quick_prime,itr_quick_prime] )
      break
    else:
      rest_n= (itr_input_list - itr_quick_prime)
      if (rest_n in quick_prime_list):
        if itr_quick_prime < rest_n:
          golid.append([itr_quick_prime, rest_n])

# 둘 차이가 적은 놈을 반환하는 로직
  answer_list = []
  for itr_goldi in golid:
    diff = (itr_goldi[1] - itr_goldi[0])
    answer_list.append([itr_goldi[0], itr_goldi[1], diff])

  temp=[]
  for itr_answer_list in answer_list:
    temp.append(itr_answer_list[2])

  min_diff = min(temp)
  for itr_answer_list in answer_list:
    if itr_answer_list[2] == min_diff:
      print(itr_answer_list[0], itr_answer_list[1])