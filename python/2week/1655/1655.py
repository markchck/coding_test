# 1 = 1 
# 1 5 = 1
# 1 2 5 = 2
# 1 2 5 10 = 2
# -99 1 2 5 10 = 2
# -99 1 2 5 10 7 = 2
# -99 1 2 5 5 10 7 = 5

# 넣을 때마다 새롭게 정렬해서 인덱스의 중간 값을 추출한는 방식 (시간 복잡도 n*logn일 듯?) 이 아니고 n* n*logn이구나
# import sys
# input = sys.stdin.readline
# N = int(input())
# items=[]
# for i in range(N):
#     items.append(int(input()))
#     items.sort()
#     if (len(items)%2 == 0): 
#         print(items[len(items)//2-1])
#     else:
#         print(items[len(items)//2])

import sys, heapq
input = sys.stdin.readline
n = int(input())

num = int(input())
print(num)
minHeap, maxHeap = [],[(-num, num)]
for i in range(n-1):
    num = int(input())
    if (num > maxHeap[0][1]):
        heapq.heappush(minHeap,num)
    else:
        heapq.heappush(maxHeap,(-num,num))
    
    
    if len(minHeap) > len(maxHeap):
        tmp = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, (-tmp,tmp))
    elif len(minHeap)+1 < len(maxHeap): #min보다 max가 2개 많아지면 그때야 떼서 min줌
        (fake,real) = heapq.heappop(maxHeap)
        heapq.heappush(minHeap,real)
    # if len(minHeap) == len(maxHeap):
    #     pass
    # elif len(minHeap) > len(maxHeap):
    #     tmp = heapq.heappop(minHeap)
    #     heapq.heappush(maxHeap, (-tmp,tmp))
    # else: #길이가 같거나, 더 멕스가 더 길면?
    #     (fake,real) = heapq.heappop(maxHeap)
    #     heapq.heappush(minHeap,real)
    print(maxHeap[0][1])
