# https://www.acmicpc.net/problem/2438

a = int(input())
for i in range(a):
  print('*'*(i+1))

# 아래 코드의 컨셉인 i와 j 2차원 배열은 c에서는 작동하는데 파이썬에선 작동 안함..print를 하면 자동으로 줄을 바꿔버려서..
# for i in range(a+1):
#   for j in range(i):
#     print('*')

# 백준에 올리면 출력형식이 잘못되었다는 에러 뜰거다. (다시한번 말하지만 파이썬은 print하고 줄을 자동으로 바꿔버림.. 고로 i가 0일때 print('*'*i)일때도 비록 나오는 *는 없지만 줄은 바뀜. 자연스레 한칸씩 밀리게 됨.)
# a = int(input())
# for i in range(a+1):
#   print('*'*i)



