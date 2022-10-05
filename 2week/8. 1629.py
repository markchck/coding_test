# https://www.acmicpc.net/problem/1629
# 3시 41분 시작 그냥 곱셈기호 쓰면 안되나?ㅋㅋ
# 어림도없다 이눔아! 시간초과

import sys
def main():
  A, B, C=map(int, sys.stdin.readline().split())
  T = A**B
  R = T%C
  print(R)
main()