class Chaining:
    class Node:
        def __init__ (self, key, data):
            self.key = key
            self.data = data
            self.next = None
    def __init__(self, size):
        self.M = size
        self.a = [None for _ in range(size+1)] #해시테이블

    def hash(self, key):
        return key % self.M
    
    def put(self, key, data):
        i = self.hash(key)
        p = self.a[i]
        while p != None: #충돌발생
            if key == p.key: #키가 같으면 값만 교체
                p.data = data
                return
            else: #키가 같지 않으면 
                p.next = self.Node(key,data)
                return
        self.a[i] = self.Node(key,data)  

    def get(self, key):
        i = self.hash(key)
        p = self.a[i]
        if p == None:
            return "데이터 없음"
        else:
            while p != None:
                if p.key == key:
                    return p.data
                else:
                    p = p.next
            return "데이터 없음"


hash = Chaining(2)
hash.put(1, "재민")
hash.put(3, "진주")
print(hash.a)
print("나온 값", hash.get(3))

        
