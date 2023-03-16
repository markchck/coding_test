# # 11. 10828 연결리스트 스택
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        tmp=self.head
        self.head = self.head.next
        return tmp.value

stack = Stack()
stack.push(1)
print(stack.pop())