# https://www.acmicpc.net/problem/8958
# 이 문제가 처음 내가 재귀의 개념을 스스로 떠올린 문제 같아서 기록

    
# 재귀 개념을 한번에 떠올린건 아니고 이렇게 [0], [1], [2]...인 상황 하나씩 수기로 써보니까 뭔가 반복되는 느낌?? 그래서 그걸 
# 묶어서 아래 코드와 같이 재귀로 돌려버림.
  # for i in range(len(N)):
  #   if N[0] == 1:
  #     seq = seq+1
  #     sum = sum+seq

  #     if N[1] ==1:
  #       seq = seq+1
  #       sum = sum + seq
  #     else:
  #       seq = seq
  #       sum = sum

  #   else:
  #     seq = seq
  #     sum = sum

  #     if N[1] ==1:
  #       seq = seq+1
  #       sum = sum + seq
  #     else:
  #       seq = seq
  #       sum = sum

# 이 코드 백준에 올리면 런타임 뜰건데 나는 ox로 안하고 1, 0으로 해서 그럼.
# 그리고 0이 아니라 'O' 특수문자 써야 백준이랑 맞음.. 
A = int(input())
for i in range(A):
  N = input()
  seq = 0
  sum = 0
  for i in range(len(N)):
    if int(N[i]) == 1:
      seq = seq + 1
      sum = sum + seq
    else:
      seq = 0
      sum = sum
  print(sum)


  

