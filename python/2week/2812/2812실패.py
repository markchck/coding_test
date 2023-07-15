# 바로 뒤에 있는 숫자랑 비교해서 작으면 죽여?
# 포인터를 두개를 두고, 앞 뒤 를  비교해서 작은거는 죽인다. 는 생각으로 짠 코드이나 실패했음..
# (실패 이유) 앞뒤로 비교하면 752 같이 5를 살려야하는데 7과 비교하기 때문에 죽어버리는 현상이 발생함..

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
items = deque(list(map(int, input().strip())))
# que에 두 개 씩 넣을거임.
que = deque([items.popleft(), items.popleft()])

k = 0
temp = deque()
while que and k != K:
    if que[0] > que[1]:
        if k == K:
            break
        que.pop()
        que.append(items.popleft())
        k += 1
    elif que[0] == que[1]:
        temp.append(que.pop())
        que.append(items.popleft())
    else:
        if k == K:
            break
        que.popleft()
        que.append(items.popleft())
        k += 1
result = temp + que + items
print("".join(map(str, result)))
