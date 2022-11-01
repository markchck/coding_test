A = int(input())
for i in range(A):
  N = input()
  seq = 0
  sum = 0 
  for i in range(len(N)):
    if N[i]=="O":
      seq += 1
      sum += seq
    else:
      seq= 0
  print(sum)