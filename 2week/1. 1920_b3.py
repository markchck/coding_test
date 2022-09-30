# https://www.acmicpc.net/problem/1920
# https://velog.io/@deannn/BOJ-백준-1920번-수-찾기-Python
N = int(input())
A = list(map(int,input().split(" ")))
M = int(input())
arr = list(map(int, input().split(" ")))

A.sort() #A정렬

for num in arr:
  left, right = 0, N-1 #컴퓨터는 0부터 센다
  isExist = False

  # 이분탐색 시작
  while left <= right: #이 생각 레알 어렵겠다.. 얼마나 반복문을 돌려야하냐? (왼쪽과 오른쪽이 역전나면 멈춰)
    mid = (left+right)//2 #지금까지 변수 설정만 했을 뿐 아무것도 한게 없음.
    if num == A[mid]:
      print(1)
      isExist = True
      break
    elif (num > A[mid]):
      left = mid +1 #와 이 부분이 왼쪽 버려네?
    else: #num<A[mid]
      right = mid-1
  if isExist == False:
    print(0)