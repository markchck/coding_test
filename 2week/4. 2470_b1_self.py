# https://www.acmicpc.net/problem/2470

# 이진탐색말고 투포인터라는 기법이 있음 :시간 복잡도는 n임. 
# https://m.blog.naver.com/kks227/220795165570 참고.
# (브루트포스는 n**2인데 투포인터는 n개면 n번 포인터가 이동하면 되기 때문에 시간복잡도 n이라 이것도 충분히 빠르다.)


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