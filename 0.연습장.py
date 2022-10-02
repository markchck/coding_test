#입력
import sys
s = sys.stdin.readline().strip()

#초기 설정 값
stack = []
tmp = 1 #곱하기를 하려면 0으로 설정하면 안되니 1로하고
res = 0 #그러면 tmp값을 출력하면 오류가 뜨니 res라는 초기값 0인 놈을 따로 또 설정

#스텍 넣기 판단하기
for i in range(len(s)):
  # 여는 괄호 stack에 넣기
  if s[i] == '(':
    tmp = tmp*2
    stack.append(s[i])
  elif s[i] == '[':
    tmp = tmp*3
    stack.append(s[i])
  # 닫는 괄호 stack에 넣기
  elif s[i] == ')':
    if not stack or stack[i-1] == '[':
      res = 0 #조건 상 괄호 쌍이 안 맞으면 무조건 0을 출력하라고 함
      break
    if s[i-1] == '(': #만약 ()이렇게 짝이 맞으면? 둘을 없애면서 최종값에 2를 추가
      res = res +tmp
      tmp//2
      stack.pop()
  else : #']'로 닫는 경우
    if not stack or stack[i-1] == "(":
      res = 0
      break
    if s[i-1] == '[':
      res = res + tmp
      tmp//3
      stack.pop()

#여는 괄호만 남아있는 예외조건 처리
if stack:
  res = 0

#결괏값 출력
print(res)

  
