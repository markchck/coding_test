# https://www.acmicpc.net/problem/2470
# 9시 41분 시작 - 11시 2분 종료(생각 못함)

import sys
def main():
  n = int(input())
  arr = list(map(int,sys.stdin.readline().split()))
  arr.sort()

  lp = 0
  rp = n-1
  lastdata = [2000001000,lp,rp] #혹시모르니 +a로 max값에 1000더 넣음. (최종 출력물임)

  while lp < rp:
    summed = arr[lp] + arr[rp] #왼쪽과 오른쪽을 더한걸 summed라고 하자.
    if summed == 0: #summed가 0이면 바로 그 값을 출력 
      print(arr[lp], arr[rp])
      return
    if abs(summed) < lastdata[0]: #summed (첫번째인자, 두번째 인자) 두 개 더한게 이전 것 보다 더 0으로 좁혀지면?
      lastdata[0], lastdata[1], lastdata[2] = abs(summed), lp, rp #새로운 값을 lastdata에 넣음.
    if summed <0:
      lp += 1
    else:
      rp -= 1
  print(arr[lastdata[1]], arr[lastdata[2]])

main()