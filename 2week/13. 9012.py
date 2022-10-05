# https://www.acmicpc.net/problem/9012
# 2시 11분

import sys
T = int(sys.stdin.readline().strip())

list_l = []
for i in range(T):
  list_l.append(sys.stdin.readline().strip())
# print(list_l[0][0] =="(")
# print(list_l)
for list in list_l:
  sum =0
  for j in range(len(list)):
    if (list[j] == "("):
      sum += 1
    else:
      sum -= 1

    if sum <0:
      print("NO")
      break

  if sum>0:
    print("NO")
  elif sum == 0:
    print("YES")
  else:
    pass