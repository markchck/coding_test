class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        self.head = None
    
    def push(self,value):
        new_node = Node()
        new_node.value = value
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        self.head = self.head.next











# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Stack:
#     def __init__(self):
#         self.head = None #(스택top이 비어있다.)
#     def push(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node
#     def pop(self):
#         tmp = self.head
#         self.head = self.head.next
#         return tmp.data

# stk = Stack()
# stk.push(1)
# # print(stk.pop())