# https://www.acmicpc.net/problem/2110
import sys

def main():
  n,c = sys.stdin.readline().split()
  n,c = int(n), int(c)
  x = [int(sys.stdin.readline().strip()) for _ in range(n)]
  x.sort()

  if c ==2:
    print(x[-1] - x[0])
    return

  result = 0
  max_len = x[-1] - x[0]
  min_len = 1

  while max_len >= min_len:
    mid_len = (max_len + min_len) //2
    house = x[0]
    count =1 

    for i in range(1, len(x)):
      if x[i] - house >= mid_len:
        count += 1
        house = x[i]
    if count >= c:
      result = mid_len
      min_len = mid_len+1
    else:
      max_len = mid_len-1
  print(result)
  return
main()