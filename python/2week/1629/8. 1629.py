# https://www.acmicpc.net/problem/1629
# 3시 41분 시작 그냥 곱셈기호 쓰면 안되나?ㅋㅋ
# 어림도없다 이눔아! 이 풀이는 시간초과

# 이 풀이가 왜 시간 초과가 뜨는지 이해하는게 중요함. 
# https://www.notion.so/markchck/5c3a66166fde46449a843250293b1cdf?v=02b784c593fe4cc1a52a15a07a1f2644&p=061c2ec05a2f42dea00936b5efa76795&pm=s
# 에서 '대체 왜 분할로 정복하면 빠르냐' 참고해
# 요약하면 2^10 할 때 2*2*2*2*2*2*2 하면 바보임 2*2*2*2*2해서 A라하고 A*A하는거지.
# 똑같이 2^5할 때 2*2를 B라하고 B*B*2하는거다.

import sys
def main():
  A, B, C=map(int, sys.stdin.readline().split())
  T = A**B
  R = T%C
  print(R)
main()