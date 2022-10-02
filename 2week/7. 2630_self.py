import sys
global white, blue
white =0
blue = 0

def main():
  N = int(sys.stdin.readline().strip())
  arr= [0]*N
  for i in range(N):
    arr[i] = (list(map(int, sys.stdin.readline().split(" "))))
  
  is_same(arr,N)
  


def cutting(arr,x,y, N) -> None:
  part1 =[(0 for _ in (N/2)) for _ in (N/2)]
  print(part1)

def is_same(arr,N):
  global white, blue
  x=0
  y=0
  for row in arr:
    for column in row:
      # 만약 배열의 첫 기준점인 0,0과 다르면 쪼개고, 같으면 종이의 색깔을 판단해.
      if row[column] != arr[x][y]:
        cutting(arr,x,y,N)
        break
      else:
        if arr[0][0]==0:
          white = white + 1
        else:
          blue = blue + 1


main(arr,N)
# # 이건 빠르긴 한데 파이썬에서밖에 못씀.
# import sys
# N= int(sys.stdin.readline().strip())
# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(arr)

