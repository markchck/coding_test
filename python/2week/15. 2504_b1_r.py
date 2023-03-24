# https://www.acmicpc.net/problem/2504
# 답안 풀이

import sys
s = sys.stdin.readline().strip()
stack = []
tmp = 1
res = 0

for i in range(len(s)):
  if s[i] == '(':
    tmp = tmp*2
    stack.append(s[i])
  elif(s[i] == '['):
    tmp = tmp*3
    stack.append(s[i])
  elif (s[i] == ')'):
    if not stack or stack[-1] == '[':
      res=0
      break
    if s[i-1] == '(':
      res = res +tmp
    # tmp = tmp // 2 
    tmp //= 2
    stack.pop()
  else: # ']' 대괄호 닫는 경우
    if not stack or stack[-1] =='(':
      res = 0
      break
    if s[i-1] =='[':
      res = res +tmp
    tmp//=3
    stack.pop()
if stack:
  res = 0
print(res)