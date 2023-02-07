# fixed length stack
stk = [None] * 5
ptr = 0

def push(value):
  global stk, ptr
  # 스택 오버플로운지 확인
  if ptr >= 256:
    print("stack overflow")
    return -1
  # 아니면 추가
  else:
    stk[ptr] = value
    ptr = ptr + 1

def pop():
  global stk, ptr
  if ptr < 0 :
    print("stack is empty")
    return -1
  else:
    ptr = ptr -1
    pop_result = stk[ptr]
    stk[ptr] = None
    return pop_result



push(1)
print(stk)
# pop()
print(pop())
print(stk)
