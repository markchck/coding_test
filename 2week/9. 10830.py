# https://www.acmicpc.net/problem/10830

import sys
N, B = map(int, sys.stdin.readline().split())
list_l=[]

def main():
  global B
  for _ in range(N):
    list_l.append(list(map(int, sys.stdin.readline().split())))
  
  answer_list=multiple(list_l, B)
  print(answer_list)


def multiple(list_l, B):
  new_list = []
  for _ in range(N):
    new_list.append([1,1])

  if B ==1:
    return matrix_mulitple(list_l, new_list)
  else:
    multiple(list_l, B-1)
    matrix_mulitple(list_l, list_l) #??
  return new_list

def matrix_mulitple(list_l, new_list):
  new_list[0][0] = list_l[0][0] * ( new_list[0][0] + new_list[1][0]) #왼쪽 상단
  new_list[0][1] = list_l[0][1] * ( new_list[0][1] + new_list[1][1]) #우측 상단
  new_list[1][0] = list_l[1][0] * ( new_list[0][0] + new_list[1][0]) #좌측 하단
  new_list[0][0] = list_l[0][0] * ( new_list[0][1] + new_list[1][1]) #우측 하단
  return new_list

main()