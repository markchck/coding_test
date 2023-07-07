import sys
input = sys.stdin.readline
que = []
def push(x):
    que.append(x)
def pop():
    if que:
      tmp = que[0]
      for i in range(len(que)-1):
          que[i] = que[i+1]
      return tmp
    else:
      return -1
def size():
   return len(que)
def empty():
   if que:
      return 0
   else: 
      return 1
def front():
    if que:
        return que[0]
    else:
        return -1
def back():
    if que:
      return que[-1]
    else:
       return -1
