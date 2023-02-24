# 컴퓨터가 괄호 연산 3(2+3(2))+2(3+2) 이런 연산을 어떻게 계산하는지 알 수 있는 문제.
import sys
input = sys.stdin.readline

string = input().split()[0]
tmp = 1
res = 0
list_a = []
for i in range(len(string)):
  char = string[i]
  if char == "(":
    tmp *= 2
    list_a.append(char)
  elif char == '[':
    tmp *= 3
    list_a.append(char)
  elif char == ')':
    if len(list_a)==0 or list_a[-1] == '[':
      res = 0
      break #브레이크를 해줘야함.
    else:
      if string[i-1] =='(':
        res += tmp
      tmp //= 2
      list_a.pop()
  else:
    if len(list_a)==0 or list_a[-1] == '(':
      res = 0
      break
    else:
      if string[i-1] =='[':
        res += tmp
      tmp //= 3
      list_a.pop()

if list_a: #엣지케이스  (()인 경우 필터링
  print(0)
else:
  print(res)