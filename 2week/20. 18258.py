# https://www.acmicpc.net/problem/18258
import sys
from collections import deque
que = deque()

N=int(sys.stdin.readline().strip())


command_l=[]
for i in range(N):
  command_l = (list(sys.stdin.readline().split()))
  # print(command_l)

  if len(command_l) ==2:
    que.append(command_l[1])
  elif(command_l[0] == "pop"):
    if len(que)==0: 
      print(-1)
    else:
      print(que.popleft())
  elif(command_l[0] == "size"):
    print(len(que))
  elif(command_l[0] == "empty"):
    if len(que) == 0:
      print(1)
    else:
      print(0)
  elif(command_l[0] == "front"):
    if not que:
      print(-1)
    else:
      print(que[0])
  elif(command_l[0] == "back"):
    if not que:
      print(-1)
    else:
      print(que[-1])
  else:
    pass


# for itr_command_l in command_l:
#   if len(itr_command_l)==2:
#     first_word = itr_command_l[0]
#     second_word = itr_command_l[1]
#   else:
#     first_word = itr_command_l[0]

#   if first_word == "push":
#     que.append(second_word)
#   elif(first_word == "pop"):
#     if len(que)==0: 
#       print(-1)
#     else:
#       print(que.popleft())
#   elif(first_word == "size"):
#     print(len(que))
#   elif(first_word == "empty"):
#     if len(que) == 0:
#       print(1)
#     else:
#       print(0)
#   elif(first_word == "front"):
#     if not que:
#       print(-1)
#     else:
#       print(que[0])
#   elif(first_word == "back"):
#     if not que:
#       print(-1)
#     else:
#       print(que[-1])
#   else:
#     pass
