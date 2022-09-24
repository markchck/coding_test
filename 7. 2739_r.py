# https://www.acmicpc.net/problem/2739

a=int(input())

for i in range(1,10):

  #표현식 1
  print(f'{a} * {i} = {a*i}')
  # print(f'{a} * {i} = {a*{i}}')

  # #표현식 2
  # print( '%i * %i = %i' %(a, i, (a*i)) )

  # #표현식 3
  # print(a, '*', i, '=', a*i)