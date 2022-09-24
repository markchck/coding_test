# https://www.acmicpc.net/problem/2675
# 난 [[abc], [/htp]]이렇게 배열안에 배열을 넣는 방식으로 풀었는데 다른 풀이보니까 5줄컷이네?
# 다른 방식으로 다시 풀어보자

N = int(input())
input_values_number=[]
input_values_stirng=[]
tmp_list =[]
result_list=[]
for i in range(N):
  S = input().split(" ")
  input_values_number.append(int(S[0]))
  input_values_stirng.append(S[1])

for i in range(len(input_values_number)):
  for itr_input_values_string in input_values_stirng[i]:
    tmp_list.append(itr_input_values_string *input_values_number[i])
  result_list.append(tmp_list)
  tmp_list=[]

for i in range(len(result_list)):
  for j in range(len(result_list[i])):
    print(result_list[i][j], end='')
  print()


