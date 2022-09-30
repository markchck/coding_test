# 10시 37분에 시작 11시 37분에 마무리

N=int(input())
A=set(map(int, input().split(" ")))
M=int(input())
B=map(int, input().split(" "))

for itr_B in B:
  if(itr_B in A):
    print(1)
  else:
    print(0)