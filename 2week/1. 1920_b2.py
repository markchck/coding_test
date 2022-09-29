# 8시 40분에 시작
N = int(input())
A_list = sorted(list(map(int, input().split(" "))))
M = int(input())
B_list = list(map(int, input().split(" ")))

mid = len(A_list)/2

def half(itr_m, len):
  if(len == 1):
    return 
  else:
    half(itr_m, len-1)
    left_A = A_list[0:len]
    right_A = A_list[len:]

for irt_m in M:
  half(irt_m, len(A_list))
