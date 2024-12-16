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
        newNode.next = self.head

    def remove(self):
        self.head = self.head.before

    # n번째 인덱스에 value 삽입
    def insertValue(self, n, value):
        pass

    def contins(self, value):
        pass

    def size():
        pass

    def isEmpty():
        pass
