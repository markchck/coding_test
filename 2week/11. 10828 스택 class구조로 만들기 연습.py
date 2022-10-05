# https://www.acmicpc.net/problem/10828
# 9시 36분 시작
class Stack:
  # 1. 기반공사
  class Empty(Exception):
    pass
  class Full(Exception):
    pass
  def __init__(self, capacity: int) -> None:
    self.stk = [None]*capacity
    self.capacity = capacity
    self.ptr = 0
  def __len__(self) ->int: #배열의 개수 셀 때의 그 len()처럼 간편하게 쓰려면 던더함수__len__을 정의해줘야함.
    return self.ptr
  def is_full(self) ->bool:
    return self.ptr >= self.capacity
  def is_empty(self) ->bool:
    return self.ptr <= 0
  
  # 2. 기능 구현
  def push(self, value):
    if self.is_full():
      raise Stack.Full
    self.stk[self.ptr] = value
    self.ptr += 1
  def pop(self):
    if self.is_empty():
      raise Stack.Empty
    self.ptr -= 1
    return self.stk[self.ptr]
  def peek(self):
    if self.is_empty():
      raise Stack.Empty
    return self.stk[self.ptr-1]
  def clear(self):
    self.ptr = 0 #이거 이해가 안됐음. 포인터가 0이면 맨처음 쌓은 데이터를 의미하는 거 아님?
  def find(self, value):
    for i in range(self.ptr, -1, -1): 
    #현재 포인터가 6이라면, -1번째까지 루프를 돌고 -1씩 줄어드는 공차를 가짐.
    #왜 6부터 -1까지냐면 range(n)하면 0부터 n-1까지 세잖아? n번째는 안들어감. 마찬가지로 range(6, -1)이라해야 6부터 0까지 센다.
      if self.stk[i] == value:
        return i
        # 인덱스 값을 반환(stk[i]를 반환해도 되긴 하는데 어차피 인자로 주어진 value랑 같은데 뭐하러 ㅋㅋ)
      return -1
  def count(self, value) ->int:
    c = 0
    for i in range(self.ptr):
      if self.stk[i] == value:
        c+=1
    return c
  def __contains__(self, value) ->bool:
    return self.count(value) > 0

  def dump(self):
    if self.is_empty():
      print("스택이 비었습니다.")
    else:
      print(self.stk[:self.ptr])

# # 3. 활용
# stack = Stack(10)

# # 스택에 값 넣기
# stack.push(1)
# stack.push(2)
# stack.push(3)

# # 스택에서 값 빼기
# # stack.pop()

# # 스택에 모든 값 불러오기
# # stack.dump()

# # 스택 맨 위 값을 불러오기
# # print(stack.peek())

# # 스택에서 3을 찾아 몇번째 Index인지 뱉기
# # print(stack.find(3))

# # 스택에서 1이 몇번 들어가 있는지 세기
# # print(stack.count(1))

# # 스택이 1을 포함고 있는지 판단하기
# # print(stack.__contains__(1))
# # print(10 in stack)

# # 스택의 길이 구하기
# print(stack.__len__())
# print(len(stack))

# # 스택 초기화하기
# # stack.clear()




import sys
N = int(sys.stdin.readline().strip())

command_l = []
for _ in range(N):
  command_l.append(list((sys.stdin.readline().split())))

print(command_l)





