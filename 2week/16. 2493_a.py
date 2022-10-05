# https://www.acmicpc.net/problem/2493

# 내 바로 뒤에 있는놈이 나보다 키가 작으면 바로 0을 내뱉는게 아니라 그 뒤엣놈들도 탐색해야하는데 그걸 구현 못했음.
# 계속 for문에 for문에 for문으로 들어가는 것 밖에 생각나지 않음.. 중도 포기
import sys
from collections import deque
deq= deque
result=deque()

N=int(input())
# deq(map(int, sys.stdin.readline().split()))
deq=deq(map(int, sys.stdin.readline().split()))
count= 0
for i in range(len(deq)-1,-1,-1):
    for j in range(i-1,-1,-1):
        if i==j:
            pass
        else:
            if deq[i]<deq[j]: #뒤에 있는 타워가 키가 더 큰 더 뒤에있는 타워를 만나면..
                result.appendleft(j+1)
                break
            else:
                # 어떻게하면 바로 뒤엣놈 말고 더 뒤엣놈들 중 나보다 키 큰애가 있는지 추가 탐색을 하게 할 수 있을까? 바로 뒤엣놈만 보고 끝내는게 아니라.
                result.appendleft(0)
print(result)