class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        popleft = self.queue[0]
        self.queue = self.queue[1:]
        return popleft
    
que = Queue()
que.enqueue(1)
que.enqueue(2)
que.dequeue()
print(que.queue)
