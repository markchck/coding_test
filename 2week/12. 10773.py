# https://www.acmicpc.net/problem/10773
# 1시 42분

import sys
K = int(sys.stdin.readline().strip())

number_list =[]
for i in range(K):
  number_list.append(int(sys.stdin.readline().strip()))

new_list = []
def push(value):
  new_list.append(value)

def pop():
  global new_list
  # new_list = new_list[:len(new_list)-1] #이렇게도 없앨 수 있음
  new_list.remove(new_list[-1])

for number in number_list:
  if number != 0:
    push(number)
  else:
    pop()
print(sum(new_list))
