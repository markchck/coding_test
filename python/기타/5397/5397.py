import sys
input = sys.stdin.readline


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.before = None


class LinkedList:
    def __init__(self):
        self.head = None  # 포인터 같은 느낌

    def add(self, value):
        newNode = Node(value)
        # 최초에는 None을 복사하기 때문에 참조가 아닌 value가 복사되지만 이후 노드들은 self.head = newNode를 거치면서 참조가 복사된다.
        newNode.before = self.head
        self.head = newNode
        newNode.next = None
        print(self.head)

    def remove(self):
        self.head = self.head.before
        print(self.head)

    def moveForword(self):
        if (self.head == None):
            print(self.head)
            return
        else:
            self.head = self.head.before
            self.head
            print(self.head)

    def moveBackword(self):
        if (self.head.next == None):
            print(self.head)
            return
        else:
            self.head = self.head.next
            print(self.head)

    def showAll(self):
        while (self.head.next != None):
            print(self.head.value)


for i in range(int(input().strip())):
    for c in list(input()):
        temp = LinkedList()
        if (c == "-"):
            temp.remove()
        elif (c == ">"):
            temp.moveBackword()
        elif (c == "<"):
            temp.moveForword()
        else:
            temp.add(c)
    print(temp.showAll())
