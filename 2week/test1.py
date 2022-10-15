# n*n배열 만드는거 엄청 헤매고.
# 배열이 범위를 벗어났다 에러?
# 각 사분면에 몫이랑 나머지 활용해서 넣는거 헤매고


import sys
N=int(sys.stdin.readline().strip())
list_a=[]
for i in range(N):
  # list_a = list(map(int, sys.stdin.readline().strip()))
  list_a.append(list(map(int, sys.stdin.readline().strip())))
count_0 = 0
count_1 = 0
error= 0


def cutting(list, N):
  global count_0, count_1, error
  half=N//2
  list_1=[]
  for _ in range(half):
    for _ in range(half):
      list_1.append([0]*half)

  list_2=[]
  for _ in range(half):
    for _ in range(half):
      list_2.append([0]*half)

  list_3=[]
  for _ in range(half):
    for _ in range(half):
      list_3.append([0]*half)

  list_4=[]
  for _ in range(half):
    for _ in range(half):
      list_4.append([0]*half)

  # list_1 = [ [0]*N for_in range(half) for _ in range(half)  ]
  # print(list_1)
  # list_2 = [ [0]*N for _ in range(half)]
  # list_3 = [ 0 for _ in range(half) for _ in range(half)]
  # list_4 = [ 0 for _ in range(half) for _ in range(half)]

  
  # standard=list[0][0]
  # if N==2:
  #   for i in range(N):
  #     for j in range(N):
  #       if standard!=list[i][j]:
  #         error= error+1
  #         cutting(list,N)
  #         break
  #   if error == 0: #만약 모든게 같다면?
  #     if standard == 0:
  #       count_0+=1  #카운트하는게 아닌것 같긴한데.. 일단 구현해보자..
  #       return count_0
  #     else:
  #       count_1+=1
  #       return count_1

  for row in range(len(list)):
    for col in range(len(list)):
      if (row//(half)<1 and col//(half)<1) : #왼쪽 상단
        list_1[row%half][col%half] =list[row][col]
      elif (row//(half)<1 and col//(half)>=1) : #우측 상단
        list_2[row%half][col%half] =list[row][col]
      elif (row//(half)>=1 and col//(half)<1) : #좌측 하단
        list_3[row%half][col%half] =list[row][col]
      else:#우측 하단
        list_4[row%half][col%half] =list[row][col]

  is_same(list_1)
  is_same(list_2)
  is_same(list_3)
  is_same(list_4)

def is_same(list):
  global count_0, count_1, error
  standard = list[0][0]
  for i in range(len(list)):
    for j in range(len(list)):
      if standard != list[i][j]:
        error = error + 1
        cutting(list, N)
        break
  if error == 0: #만약 모든게 같다면?
    if standard == 0:
      count_0+=1  #카운트하는게 아닌것 같긴한데.. 일단 구현해보자..
      return count_0
    else:
      count_1+=1
      return count_1
        
        

def main():
  global list_a, N
  is_same(list_a)
  print(count_0, count_1)
main()