# https://www.acmicpc.net/problem/10830
import sys
N, B = map(int, sys.stdin.readline().split())
list_l=[]
new_list = []
for _ in range(N):
  new_list.append([1,1])

def main():
  global B
  for _ in range(N):
    list_l.append(list(map(int, sys.stdin.readline().split())))
  
  answer_list=multiple(list_l, B)
  print(answer_list)


def multiple(list_l, B):
  if B ==1:
    return list_l
  else:
    multiple(list_l, B-1) #중간에 간섭이 생겨버리네?? 
    new_list[0][0] = list_l[0][0] * ( list_l[0][0] + list_l[1][0]) #왼쪽 상단
    new_list[0][1] = list_l[0][1] * ( list_l[0][1] + list_l[1][1]) #우측 상단
    new_list[1][0] = list_l[1][0] * ( list_l[0][0] + list_l[1][0]) #좌측 하단
    new_list[0][0] = list_l[0][0] * ( list_l[0][1] + list_l[1][1]) #우측 하단
  return new_list

main()

# 코드 이상해서 바꿀건데 혹시모르니 복사
# import sys
# N, B = map(int, sys.stdin.readline().split())
# list_l=[]
# # new_list = []
# # for _ in range(N):
# #   new_list.append([1,1])

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
#     matrix_mulitple(list_l, new_list)
#   return new_list

# def matrix_mulitple(list_l , new_list): #왼쪽이 곱하는 행렬, 오른쪽이 곱해진 행렬
#   new_new_list = []
#   for _ in range(N):
#     new_new_list.append([1,1])

#   new_new_list[0][0] = list_l[0][0] * ( new_list[0][0] + new_list[1][0]) #왼쪽 상단
#   new_new_list[0][1] = list_l[0][1] * ( new_list[0][1] + new_list[1][1]) #우측 상단
#   new_new_list[1][0] = list_l[1][0] * ( new_list[0][0] + new_list[1][0]) #좌측 하단
#   new_new_list[0][0] = list_l[0][0] * ( new_list[0][1] + new_list[1][1]) #우측 하단
#   return new_new_list

main()