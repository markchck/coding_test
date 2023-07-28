# 매번 최소를 가져오고 덧셈은 누적하면 될 듯?
# 합친 카드를 다시 넣는 작업 필요할 듯 (힙 써야겠다. 매번 정렬 다시 할 순 없음)
import sys
import heapq
input = sys.stdin.readline
N = int(input())
cards = []
for _ in range(N):
    cards.append(int(input()))
heapq.heapify(cards)
sum = 0
while len(cards) >= 2:
    now = heapq.heappop(cards)
    next = heapq.heappop(cards)
    sum += (now+next)
    heapq.heappush(cards, now+next)
print(sum)


# 10 + 20 = 30
# 30 + 40 = 70
# 70 + 50 = 120
# 220
