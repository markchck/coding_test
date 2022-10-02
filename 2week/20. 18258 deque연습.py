# https://www.acmicpc.net/problem/18258
from collections import deque
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
# stack.appendleft(1)
# stack.clear()
stack.insert(2,4)
stack.remove(2)
stack.reverse()
print(stack.count(1))
print(stack)