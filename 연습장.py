import sys
import heapq
input = sys.stdin.readline
N = int(input())
items = []

for _ in range(N):
    items.append(list(map(int, input().split())))

D = int(input())

roads = []
for item in items:
    house, office = item
    if abs(house-office) <= D:
        item.sort()
        roads.append(item)
roads.sort(key=lambda x: x[1])  # office를 기준으로

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        atLeast = road[1] - D
        while heap[0][0] < atLeast:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))
print(answer)
