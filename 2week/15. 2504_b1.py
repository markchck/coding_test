# https://www.acmicpc.net/problem/2504
# 답안 풀이

import sys
s = sys.stdin.readline().strip()
stack = []
tmp = 1

for i in range(len(s)):
  if s[i] == '(':
    tmp = tmp*2
    stack.append(s[i])
  elif(s[i] == '['):
    tmp = tmp*3
    stack.append(s[i])
  elif (s[i] == ')'):
    if not stack or stack[-1] == '[':
      break
    if s[i-1] == '(':
      tmp =tmp 
