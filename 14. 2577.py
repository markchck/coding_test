# https://www.acmicpc.net/problem/2577

# result_list : 곱하기 결과 값을 문자열로 변호나 시킨 것
# counting : 예) 0이 몇 번 들어있는지 결괏값 들어있는 곳
# answer_lists : 0,1,2,3,4...으 counting값이 배열로 들어갈 곳
a = int(input())
b = int(input())
c = int(input())

result = a*b*c
result_lists=str(result)
answer_lists = []
for i in range(10):
  counting = 0
  for result_list in result_lists:
    if(i == int(result_list)):
      counting = counting + 1
  answer_lists.append(counting)

for answer_list in answer_lists:
  print(answer_list)