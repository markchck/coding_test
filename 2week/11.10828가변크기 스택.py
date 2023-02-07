
#! 가변 크기 스택 구현

stk = []
ptr = 0

def push(value):
  global stk, ptr
  ptr = ptr+1
  new_stk = [None]*ptr
  new_stk[ptr -1] = value
  new_stk = new_stk[len(new_stk)-1:]
  stk = stk + new_stk
  return stk

def pop():
  global ptr, stk
  ptr=ptr-1
  pop = stk[ptr]
  stk = stk[:ptr]
  return pop


push(1)
push(2)
push(3)
pop()
print(stk)
  


# # fixed length stack
# stk = [None] * 5
# ptr = 0

# def push(value):
#   global stk, ptr
#   # 스택 오버플로운지 확인
#   if ptr >= 256:
#     print("stack overflow")
#     return -1
#   # 아니면 추가
#   else:
#     stk[ptr] = value
#     ptr = ptr + 1

# def pop():
#   global stk, ptr
#   if ptr < 0 :
#     print("stack is empty")
#     return -1
#   else:
#     ptr = ptr -1
#     pop_result = stk[ptr]
#     stk[ptr] = None
#     return pop_result



# push(1)
# print(stk)
# # pop()
# print(pop())
# print(stk)
