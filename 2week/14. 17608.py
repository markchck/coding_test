# https://www.acmicpc.net/problem/17608
# 3시 50 시작

import sys
N=int(sys.stdin.readline().strip())

number_l=[]
for i in range(N):
  number_l.append(int(sys.stdin.readline().strip()))

length = len(number_l)
last_bar=number_l[-1]
sum =1  #자기자신은 무조건 보이는거니까 +1

for i in range(length-1, -1, -1):
  if last_bar < number_l[i]:
    sum +=1
    last_bar = number_l[i]
print(sum)