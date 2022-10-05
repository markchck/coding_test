# https://www.acmicpc.net/problem/2493

# 내 바로 뒤에 있는놈이 나보다 키가 작으면 바로 0을 내뱉는게 아니라 그 뒤엣놈들도 탐색해야하는데 그걸 구현 못했음.
# 계속 for문에 for문에 for문으로 들어가는 것 밖에 생각나지 않음.. 중도 포기
# 이거 안되는거네.. 안된다기보다는 노가다임.
# 왜냐 내 바로 뒤에 있는 놈이 나보다 키가 작았어 그럼 그 뒤엣놈들을 대상으로 for문을 하나 새로 만들어서 크기를 비교해야지? 그러다가 나보다 키큰놈을 하나 만났어. for문은 종료되고 result에 값을 하나 추가했지?
# 그리고 for문을 새로 만드는 작업을 내 뒤엣놈이 나보다 키가 작을 때마다 반복해야함.
# 문제의 조건을 보면 N은 50만까지 들어올 수 있대. 최악의 경우(막대가 1부터 50만까지 오름차순으로 되어있다면?) for문 50만개 만들어야함.
# 재귀를 쓰면 코드의 양은 줄일 수 있을진 몰라도 재귀를 쓴다고 탐색을 덜하는건 아니니 50만*49만*48만*47만.....2번 만큼 데이터를 탐색하는 대참사가 발생할 수 있다.
# 결론 전혀 다른 접근법이 필요하다.
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