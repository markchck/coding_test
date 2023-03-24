# https://www.acmicpc.net/problem/2470
# 9시 41분 시작 - 11시 2분 종료(생각 못함)
# 이진탐색말고 투포인터라는 기법이 있음 :시간 복잡도는 n임. 
# https://m.blog.naver.com/kks227/220795165570 참고.
# (브루트포스는 n**2인데 투포인터는 n개면 n번 포인터가 이동하면 되기 때문에 시간복잡도 n이라 이것도 충분히 빠르다.)

# 복습할 때 다시보니까 난 이 풀이를 이진탐색풀이라고 생각했는데 (while lp<rp보고)
# 그게 아니고 투포인터 풀이네. 왜냐 반을 버리는 로직이 없잖아? 잘봐봐 
# 근데 이 풀이가 이진 탐색 풀이보다 훨 간단하긴 하네..
import sys
def main():
  n = int(input())
  arr = list(map(int,sys.stdin.readline().split()))
  arr.sort()

  lp = 0
  rp = n-1
  last_data = [20000004000 ,lp ,rp]
  while lp < rp:
    sum= arr[lp] + arr[rp]
    # 둘 차이가 딱 0이 아닌 경우에는 최대한 근사한 값을 뽑아야하는데 그 로직임.
    if abs(sum) <last_data[0]: #전과비교해서 뭔가 당겨졌을 때
      last_data[0] = abs(sum)
      last_data[1] = arr[lp]
      last_data[2] = arr[rp]
    if sum == 0: #이 보통 이진 탐색 문제는 두개의 조건을 만족 시켜야해서 sum이 0이라고 다른 조건도 만족시키는지 알 수 없기 때문에 sum >= 0 이렇게 써야하지만 이 문제는 같기만 하면 되니까 sum == 0만 따로 빼도 됨. 
      print(arr[lp], arr[rp])
      return
    elif sum > 0: #sum이 0보다 크면 0과 가깝게하기 위해 rp를 줄여줄 필요가 있음.
      rp = rp -1
    else:
      lp = lp +1
  print(last_data[1], last_data[2])
main()


# import sys
# def main():
#   n = int(input())
#   arr = list(map(int,sys.stdin.readline().split()))
#   arr.sort()

#   lp = 0
#   rp = n-1
#   lastdata = [2000001000,lp,rp] #혹시모르니 +a로 max값에 1000더 넣음. (최종 출력물임)

#   while lp < rp:
#     summed = arr[lp] + arr[rp] #왼쪽과 오른쪽을 더한걸 summed라고 하자.
#     if summed == 0: #summed가 0이면 바로 그 값을 출력 
#       print(arr[lp], arr[rp])
#       return
#     if abs(summed) < lastdata[0]: #summed (첫번째인자, 두번째 인자) 두 개 더한게 이전 것 보다 더 0으로 좁혀지면?
#       lastdata[0], lastdata[1], lastdata[2] = abs(summed), lp, rp #새로운 값을 lastdata에 넣음.
#     if summed <0:
#       lp += 1
#     else:
#       rp -= 1
#   print(arr[lastdata[1]], arr[lastdata[2]])

# main()