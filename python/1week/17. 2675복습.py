# 입력을 반복횟수와 문자열로 분리하고
# 문자열 * 반복횟수로 print

n=int(input())
for i in range(n):
  a,b = input().split(' ')
  multi = int(a)
  for s in b:
    print(multi * s, end='')
  print()




