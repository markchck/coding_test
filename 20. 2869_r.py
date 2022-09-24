# https://www.acmicpc.net/problem/2869

A, B, V=map(int, input().split(" "))
divide = (V-A)/(A-B)
integer = (V-A)//(A-B)
rest = divide-integer
if V-A == 0:
  print(1)
else:
  if (integer)>0:
    if(rest == 0):
      print(integer+1)
    else:
      print(integer+1+1)
  else:
    print(integer+1+1)
