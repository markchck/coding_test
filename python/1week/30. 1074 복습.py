# 시간 초과 뜨는 풀이이긴하나 로직을 이해하는데 많은 도움이 되는 풀이임.
# 시간 초과가 뜨는 이유는 재귀로 찾는다하더라도 2^N승 개의 사각형을 다 돌아야하기 때문임.
# https://my-coding-notes.tistory.com/411 이 사람 설명 보면 한 칸 씩 보지않고 n^2한번에 계산하지 않으면 시간초과 뜨는 이유 설명

# import sys
# input = sys.stdin.readline
# count = 0
# N,R,C = map(int, input().split())

# def recursion(n,r,c):
#     global count
#     if n == 2: #종료조건
#         #A구역(n이 2이면 어떻게 하지?)
#         if r == R and c == C: #2사분
#             print(count)
#             return
#         count +=1
#         if r == R and c +1 ==C: #1사분
#             print(count)
#             return
#         count +=1
#         if r +1 == R and c  ==C: #3사분
#             print(count)
#             return
#         count +=1
#         if r+1 == R and c+1 ==C: #4사분
#             print(count)
#             return
#         count +=1
#     else:
#         #B구역
#         print("1"*n+"hi")
#         #재귀구역
#         recursion(n/2, r, c) #2사분
#         recursion(n/2, r, c + (n/2)) #1사분
#         recursion(n/2, r + (n/2), c) #3사분
#         recursion(n/2, r+(n/2), c+(n/2)) #4사분
#         print("1"*n+"bye")
#         #C구역

# recursion(2**N,0,0) #카운트를 뱉는 함수


# 정답 풀이
import sys
count = 0

def z(n,x,y):
  global count

  if not(x <= r < x+n and y <= c <y+n): #이부분에서 시간을 대폭 절약함
    count += n**2
    return

  if x == r and y ==c:
    print(int(count))
    return

  else:
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)

n, r, c = map(int, sys.stdin.readline().split(' '))
z(2 ** n, 0, 0)
