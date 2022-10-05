# https://www.acmicpc.net/problem/10830
#실패! 했으나 결국 성공!!(행렬 제곱 계산기 완성!! 물론 분할의 개념을 쓰지 않았기에 시간 초과 뜰거고 심지어 1000으로 나누지도 않았음. 하지만 내힘으로 재귀를 써서 행렬 계산기를 풀었다는거에 의미가 있음.)

import sys
N, B = map(int, sys.stdin.readline().split())
list_l=[]

list_r = []
for _ in range(N):
  list_r.append([1,1])

def main():
  global B
  for _ in range(N):
    list_l.append(list(map(int, sys.stdin.readline().split())))
  
  answer_list=multiple(list_l,list_r, B)
  print(answer_list)


def multiple(list_l, list_r, B):
  if B ==1:
    return list_l
  else:
    result=matrix_multiple(multiple(list_l, list_r, B-1),list_l)    
    return result 
    #내 의도는 retrun값이 다시 왼쪽,우측,좌측 행렬곱한는 과정을 밟아서 곱해지고 다시 multiple()함수로 올라가고 이런 그림을 원했으나.. 구현이 안됨.(그리고 이렇게 복잡하게 풀리가 없음!)

def matrix_multiple(list_l, list_r):
    result=[[0]*N for _ in range(N)]
    for i in range(N):
      for j in range(N):
        for k in range(N):
          result[i][j] = result[i][j]+ list_l[i][k]*list_r[k][j]
    # # 행렬 곱셈을 이렇게 하면 구할 수 있을거라 생각했는데 이거 잘봐.. 2*2행렬만 곱하지 3*3은 안되잖아?
    # result[0][0] = list_l[0][0] * list_r[0][0] + list_l[0][1]*list_r[1][0] #왼쪽 상단
    # result[0][1] = list_l[0][0] * list_r[0][1] + list_l[0][1]*list_r[1][1] #우측 상단
    # result[1][0] = list_l[1][0] * list_r[0][0] + list_l[1][1]*list_r[1][0] #왼쪽 하단
    # result[1][1] = list_l[1][0] * list_r[0][1] + list_l[1][1]*list_r[1][1] #우측 하단
    return result
main()

# 2제곱근까지는 되는데 3제곱근ㄱ부터는 작동하지 않음.. 2제곱한 결과에 행렬 1,2,3,4를 곱하는 과정이 생각보다 어렵거나 불가능하거나..
# 얕은 복사 깊은 복사 개념이 추가 됐는데.. 보통 복사는 얕은 복사(주소값만 복사를 해서 원본이 바뀌면 둘 다 바뀌어버림. 그래서 행렬끼리 곱하면 list_l[0][0] * list_l[0][0] + list_l[0][1]*list_l[1][0]를 통해서 왼쪽 상단을 [0][0]자리를 바꿔놓으면
# 나머지 우측 상단,좌측하단 우측 하단 모두 [0][0]을 곱할 때 사용하는 놈들 전부 좌측상단의 바뀌어버린 값으로 계산을 하게 됨 그래서 깊은 복사로 별개취급을 해줘야하는 상황이 발생함.  

# 코드 이상해서 바꿀건데 혹시모르니 복사
# import sys
# N, B = map(int, sys.stdin.readline().split())
# list_l=[]
# # list_r = []
# # for _ in range(N):
# #   list_r.append([1,1])

# def main():
#   global B
#   for _ in range(N):
#     list_l.append(list(map(int, sys.stdin.readline().split())))
  
#   answer_list=multiple(list_l, B)
#   print(answer_list)


# def multiple(list_l, B):
#   if B ==1:
#     return list_l
#   else:
#     multiple(list_l, B-1)
#     matrix_mulitple(list_l, list_r)
#   return list_r

# def matrix_mulitple(list_l , list_r): #왼쪽이 곱하는 행렬, 오른쪽이 곱해진 행렬
#   new_list_r = []
#   for _ in range(N):
#     new_list_r.append([1,1])

#   new_list_r[0][0] = list_l[0][0] * ( list_r[0][0] + list_r[1][0]) #왼쪽 상단
#   new_list_r[0][1] = list_l[0][1] * ( list_r[0][1] + list_r[1][1]) #우측 상단
#   new_list_r[1][0] = list_l[1][0] * ( list_r[0][0] + list_r[1][0]) #좌측 하단
#   new_list_r[0][0] = list_l[0][0] * ( list_r[0][1] + list_r[1][1]) #우측 하단
#   return new_list_r

main()