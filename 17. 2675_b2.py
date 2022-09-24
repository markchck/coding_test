# https://www.acmicpc.net/problem/2675
# 파이썬은 문자열에서 += 개념 적용되네?

S = int(input())
for i in range(S):
  a, b = input().split(" ")
  result =''
  for i in range(len(b)):
    result = result + b[i]*int(a)
  print(result)
