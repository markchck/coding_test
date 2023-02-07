#큐 구현

# 고정크기 큐 구현(포인터를 활용해 보겟음)
queue = [None] *3
ptr = 0

def enqueue(item):
  global ptr
  queue[ptr] = item
  ptr = ptr + 1

def dequeue():
  global ptr
  pop_left = queue[0]

  #[1,2] ptr = 2 
  for i in range(ptr-1):
    queue[i] = queue[i+1]
  ptr = ptr -1
  queue[ptr] = None

  return pop_left

enqueue(1)
enqueue(2)
enqueue(3)
print(queue)
dequeue()
print(queue)
print(ptr)

