#큐 구현

# 가변 크기 큐 구현 (생으로 큐만 구현)

queue = []

def enqueue(item):
  queue.append(item)
def dequeue():
  global queue
  pop_left = queue[0]
  for i in range(len(queue)-1):
    #[1,2]를 [1]로 바꾸는 상황
    #len=2 i는 0까지만 돈다. (len(queue)-1 = 1)
    #i = 0, q[0] = q[1] =2
    queue[i] = queue[i+1]
  queue = queue[:len(queue)-1] #!이 부분 슬라이싱 덕분에 deque해도 [2, 3, None] 이 놈처럼 None 안남고  깔끔하게 [2,3] 남는다.
  return print(pop_left)

enqueue(1)
enqueue(2)
enqueue(3)
print(queue)
dequeue()
dequeue()
print(queue)



# # 고정크기 큐 구현(포인터를 활용해 보겟음)
# queue = [None] *3
# ptr = 0

# def enqueue(item):
#   global ptr
#   queue[ptr] = item
#   ptr = ptr + 1

# def dequeue():
#   global ptr
#   pop_left = queue[0]

#   #[1,2] ptr = 2 
#   for i in range(ptr-1):
#     queue[i] = queue[i+1]
#   ptr = ptr -1
#   queue[ptr] = None

#   return pop_left

# enqueue(1)
# enqueue(2)
# enqueue(3)
# print(queue)
# dequeue()
# print(queue)
# print(ptr)

