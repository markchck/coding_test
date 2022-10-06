import heapq
A=heapq()
A = [6,4,5,236,7,8]

heapq.heapify(A)
heapq.heappop(A)
heapq.heappush(A,3)
print(A)

# from collections import deque
# A=deque()
# A.append(1)
# print(A)