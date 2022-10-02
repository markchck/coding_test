n = int(input())
stk = []
answer = ()

for i in range(n):
  num = int(input())
  while stk and stk[-1] <= num:
    stk.pop()
  stk.append(num)
answer = len(stk)
print(answer)