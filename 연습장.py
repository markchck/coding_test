class DoubleHasing:
    def __init__(self, size):
        self.M = size
        self.a = [None for x in range(size+1)] #0은 안쓰고 1~13까지 쓰려고 size+1
        self.d = [None for x in range(size+1)] #데이터 넣는 d구나!
        self.N = 0
    def hash(self, key):
        return key % self.M
    def put(self, key, data): #삽입연산
        i= self.hash(key) #초기위치
        d= (key % 7)+1 #이건 왜 하드코딩?(size보다 작은 소수 구하면 될 듯)
        j=0 #차수를 의미하는 j
        while self.N < self.M:
            postion=(i+j*d)%self.M #1,2차 해싱 반영한 버킷의 최종 위치
            # 최초 진입한 버킷의 공실여부 확인
            if self.a[postion] == None:
                # 여기에 넣으면 되고
                self.a[postion] = key
                self.d[postion] = data
                self.N +=1
                return
            if self.a[postion] == key:
                self.d[postion] = data
                return
            else:
                j+=1
        return

    def get(self, key):
        i= self.hash(key)
        d= 7 - (key % 7)
        j=0 

        while j < self.M:
            postion=(i+j*d)%self.M
            if self.a[postion] == key:
                return self.d[postion]
            else:
                j+=1
        return "no data"

hash=DoubleHasing(1)

hash.put(1, "재민")
hash.put(14, "진주")
print("hash테이블 인덱스", hash.a)

print("hash테이블 데이터", hash.d)
print(hash.get(1))
print(hash.get(14))
print(hash.get(16))
