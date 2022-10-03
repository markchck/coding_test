# https://www.acmicpc.net/problem/2110
# self연습

# 이진탐색은 무엇을 기준으로 절반을 버리는 이진탐색을 할것인가? 이게 핵심인듯.
# 이 문제는 설치간격을 midlength = (maxlenth - minlength)를 기준으로 삼아서 이진 탐색함.

import sys
def main():
  n,c = sys.stdin.readline().split()
  n,c = int(n), int(c)
  x = [int(sys.stdin.readline().strip()) for _ in range(n)]
  x.sort()

  max_length = x[-1] - x[0]
  min_length = 1

  while min_length <= max_length:
    count = 1
    house = x[0]
    mid_length = (max_length + min_length)//2 #mid_len길이 간격으로 설치해봅시다! (1간격으로 설치하면 멍청한거 ㅇㅈ?) (max_len간격으로 설치해도 멍청한거 ㅇㅈ?)그래서 중간 값으로 설치해보자!
    for i in range(1, len(x)):
      if x[i] >= house +mid_length: #기준되는 집(초깃값은 0)+mid_length
        count=count+1
        house = x[i]

    #이 부분 나무자르기에서도 똑같이 나왔던 부분임. 준호는 이 코드를 똑같이 반복했음. (따라서 흉내내야하는 코드임)
    #먼저 count == c 하고 break로 if문 빠져나오는 건 틀림. 왜냐? 문제의 조건을 잘보면..C개의 공유기를 설치하고(조건1) + 인접한 공유기의 거리를 최대로(조건2)라서 공유기의 개수 조건은 충족했다하더라고 인접한 공유기의 거리를 최대로 했는지 여부는 알 수 없다.
    #그럼 언제 모든 경우를 다 돌려봤다고 판단할 수 있냐? -> while문이 min > max가 되어서 탈출될 때. (만약 min < max 심지어 == 상태라고 하더라도 여전히 min은 오른쪽으로 max는 왼쪽으로 올 수 있는 여지가 남아있는 거다 = 루프가 한 번 더 돌 여지가 남아있다는 소리. 오로지 min>max인 경우(서로 교차되는 경우)만 모든 경우를 다 돌아서 여지가 없는 상태이다.) 
    if count>=c: #count가 너무 많다? 설치거리인 mid_length가 너무 짧았다. 즉 min을 키워서 mid를 늘려야한다.
      result = mid_length  # 이 코드도 똑같이 나무자르기에서 나왔던 코드인데 뭐하는 코드이냐면 count == c인 경우, 위에서 말했듯이 c개의 공유기는 설치했지만 최대는 아닐 수 있어서 한번 더 돌아야한다고 햇지? 근데 돌았는데 답이 아닐수도 있잖아? 그래서 result값을 일단 저장 시켜 놓는거다. 한번 더 돌렸다가 아예 조건이 성립하지 않았을 때 전으로 되돌릴수는 없어도 result를 미리 저장해놧으니 그걸 출력하면 되잖아?
      min_length = mid_length + 1
    else: #count가 적다? 설치해야하는 공유기 다 설치 못했다. mid_length를 너무 넓게 잡았다. 즉 max를 늘려야한다.
      max_length = mid_length -1
  print(result)

main()