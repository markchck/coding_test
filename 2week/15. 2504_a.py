# https://www.acmicpc.net/problem/2504
# 4시 30분 시작 ~ 1시간 고민했으나 못품


import sys 
sum = 0
list= []
string = sys.stdin.readline().strip()
for i in range(len(string)):
  if string[i] == "(":
    list.append(2)
  elif(string[i] == ")"):
    list.append(-2)
  elif(string[i] == "["):
    list.append(3)
  else:
    list.append(-3)

for l in list:
  l 
print(list)
