
no=0
front = 0
end = 0
capacity = 20
que = [None]*capacity

def is_full():
    return no>=capacity
def is_empty():
    return no <= 0

def enqueue(value):
    global end, front, capacity, que, no
    if is_full():
        return -1
    no +=1
    que[end] = value
    end +=1
    if end == capacity:
        end = 0

def dequeue():
    global end, front, capacity, que, no
    if is_empty():
        return -1
    no-=1
    x = que[front]
    front += 1
    # que = que[front:]

    if front == capacity:
        front = 0
    return x

enqueue(1)

enqueue(2)

enqueue(3)
# print(que)


print(dequeue())
# print(que)

print(dequeue())
# print(que)
