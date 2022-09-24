# https://www.acmicpc.net/problem/4344

# sum = 0
# test_number = int(input())
# student_number = int(input())

# for i in range(test_number):
#   List = list(map(int, input().split(" ")))

#   for list in List:
#     sum = sum + list


test_number = int(input())
result_list=[]
for i in range(test_number):
  li = list(map(int,input().split(" ")))
  del li[0]
  total = 0
  length = len(li)
  total = sum(li)
  # for l in li:
  #   sum = sum+l
  average = total/length

  above_average = []

  for r in li:
    if (r>average):
      above_average.append(r)
  target_lenth = len(above_average)
  result = round((target_lenth/length)*100,3)
  result_list.append(result)

for i in result_list:
  output = format(i,'.3f')
  # print(type(format(i,'.3f')))
  # print(type(output))
  # print(output,'%')
  print('%s%%' %(output))
  # print(f'{output}%')