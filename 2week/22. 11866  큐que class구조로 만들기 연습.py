# 프로그램 관점에서 보면 큐가 스텍보다는 구현하기 어려운듯?
# 현실세계에서는 선착순이 거의 진리이지만 프로그램은 최근에 입력한걸 먼저 처리하는게 더 편함.
# 배열을 생각해봐. append하면 뒤에 쌓이지? 근데 맨 앞에 있는 놈을 없앤다 생각해봐. 그럼 다 한칸씩 앞으로 땡겨줘야함.(비효율 발생)
# 그런 비효율을 막기위해 코드는 배열보다 복잡해지지만 링버퍼 형태(프로그램적 생각은 아니지만 동그란 원을 생각)로 데이터를 쌓는거임.
# 그럼 앞에 것을 뺀다해도 순서를 다 바꿔주지 않아도 됨.
# 자료구조와 함께 배우는 알고리즘 입문 p 176근방 참고하셈.

from typing import Any #(Anything의 Any를 주석으로 쓰고 싶은데 안되니 임포트해옴.)
class FixedQueue:
  class Empty(Exception):
    pass

  class Full(Exception):
    pass

  def __init__(self, capacity: int) -> None:
    self.no = 0 #현재 데이터의 개수
    self.front = 0#맨 앞 원소의 커서 (입구녕)
    self.rear = 0 #맨 끝 (똥구녕) 좌약 넣는다고 생각하셈. (똥구녕에 넣어서 입구녕으로 나옴)
    self.capacity = capacity #큐의 전체 크기
    self.que = [None] *capacity #큐의 본체 (아 큐든, 스택이든, 덱이든 배열[]을 뼈대로 하고 그걸 변형시키는 거군)

  def __len__(self) -> int:
    return self.no

  def is_empty(self) ->bool:
    return self.no <= 0 #==0으로 쓰면 에러가 날 수 있다고 꼭 0이하로 쓰라고 함.

  def is_full(self) -> bool:
    return self.no>= self.capacity

  def enque(self, x: Any)->None:
    if self.is_full():
      raise FixedQueue.Full
    self.que[self.rear] = x #좌약 x를 똥구녕에 집어 넣는다.
    self.rear += 1 #그리고 다음 똥구녕의 위치를 +1로 정해준다. 
    self.no +=1
    if self.rear ==self.capacity:
      self.rear = 0  #이게 ㄹㅇ 특이함. 바로 이 부분 때문에 링(원형)이라고 하는거구나. 좌약이 똥구녕 끝까지 꽉 찼으면? 똥구녕의 좌표를 0 즉 입으로 바꿈. (똥구녕과 입구녕이 연결되어 원이 만들어지는 순간)

  def deque(self) ->Any:
    if self.is_empty():
      raise FixedQueue.Empty
    x=self.que[self.front] #큐의 입구녕 위치의 값을 x라하고 return x로 반환하는데..
    self.front +=1
    self.no -= 1
    if self.front ==self.capacity: #만약 입구녕이 똥꾸녕까지 도착했으면 입구녕을 다시 0으로 해주면 입구녕 원래 위치로 감. (입구녕 보다 아래 있을 수는 없잖아)
      self.front=0
    return x

  def peek(self) -> Any:
    if self.is_empty():
      raise FixedQueue.Empty
    return self.que[self.front]

  def find(self, value: Any) -> Any:
    for i in range(self.no):
      index = (i+self.front) % self.capacity  #와 이 생각은 정말.. 천재적이다. 나머지를 활용해서 i값이 7~11까지 조회하고 0부터~6까지 조회하게 만들었음.
      if self.que[index] == value:
        return index
    return -1
  
  def count(self, value: Any) -> bool:
    c = 0
    for i in range(self.no):
      index = (i+self.front) % self.capacity
      if self.que[index] == value:
        c += 1
    return c
  
  def __contains__(self, value: Any) ->bool:
    return self.count(value)
  
  def clear(self):
    self.no = self.front = self.rear = 0
  
  def dump(self) ->None:
    if self.is_empty():
      print("큐가 비었습니다.")
    else:
      for i in range(self.no):
        index = (i+self.front)% self.capacity
        print(self.que[index], end='')
      print()


que=FixedQueue(10) #10개짜리 큐를 미리 생성하고

que.enque(1)
que.enque(2)
que.enque(3)
que.deque()
# print(que.find(2))
# print(2 in que)
# print(que.__contains__(2))
que.clear()
print(que.peek())
que.dump()