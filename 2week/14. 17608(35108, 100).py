#전부 스택에 넣고 팝을 하면서 맨 뒤를 팝한 숫자와 그다음 맨 뒤를 팝한 놈의 크기 비교를 한다.
#먼저 팝한게 나중에 팝한것 보다 크면 기준은 여전히 먼저 팝한놈. 나중에 팝한게 더 크면 기준은 나중에 팝한놈. 같으면 기준은 아무놈이나
#그리고 카운트는 1부터 시작하고 나중에 팝한 놈이 클 때만 카운트 +1이 된다.

import sys
input = sys.stdin.readline
list_a = []
count = 1

N = int(input())
for i in range(N):
  list_a.append(int(input()))

standard = list_a[-1]

while list_a:
  compare=list_a.pop()
  
  if standard >= compare:
    pass
  else:
    standard= compare
    count+=1

print(count)