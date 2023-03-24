import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
        # return heapq.heappop(self._queue)[-1]

# Example usage
q = PriorityQueue()
q.push("item1", 1)
q.push("item2", 4)
q.push("item3", 2)

print(q._queue)
print(q.pop())