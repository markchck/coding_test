# https://www.acmicpc.net/problem/11279
# import sys
# import heapq as hq

# numbers = int(input())
# heap = []

# for i in range(numbers):
#     num = int(sys.stdin.readline())
#     # print(num)
#     if num >0:
#         hq.heappush(heap,(-num,num)) #-를 하여 제일 큰 값이 맨 앞에 가도록 한다 (힙함수는 맨  앞-num을 기준으로 정렬하고 최소 힙정렬이 디폴트기 때문에 -7, 7 묶음이 가장 높은데 위치함. 거기서 두 번째 숫자인 7을 추출하면 최대 힙 정렬과 같음)
#     else:
#         if heap:
#            print(hq.heappop(heap)[1]) #맨앞에 수를 꺼내는데 value값을 꺼낸다 (-5,5)
#         else:
#            print(0)


import sys
import heapq as hq

numbers = int(input())
heap = []

for i in range(numbers):
    num = int(sys.stdin.readline())
    # print(num)
    if num >0:
        hq.heappush(heap,(-num,num)) #-를 하여 제일 큰 값이 맨 앞에 가도록 한다
    else:
        if heap:
           print(hq.heappop(heap)[1]) #맨앞에 수를 꺼내는데 value값을 꺼낸다 (-5,5)
        else:
            print(0)