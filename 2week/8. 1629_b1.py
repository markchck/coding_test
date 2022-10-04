# https://www.acmicpc.net/problem/1629
# 제곱을 재귀로 바꿔서 구현해봤음.  

# 이거 반례 줄게 2 10 7 넣으면 4나오는데 답은 2다. (계속 틀렸습니다가 나오길래.. 밑에 수정 풀이)
# multiple(a,b//2)*a 라고 되어있는데 이부분이 잘못 됐음. multi() * multi() 꼴이 되어야함. 2의 10승하면 1024여야하는데 32가 나옴.

# import sys
# a,b,c=map(int, sys.stdin.readline().split())

# def main(a,b,c):
#   result =multiple(a,b)
#   print(result%c)
  
# def multiple(a,b):
#   if b==1:
#     return a
#   elif (b%2 == 0): #b가 짝수이면?
#       return multiple(a,b//2)*a
#   else: #홀수이면?
#       return multiple(a,(b//2+1))*a
#     # return multiple(a, b-1) * a

# main(a,b,c)



# 이거 분할정복 제대로 구현한 제곱계산기 맞는데..그래도 시간 초과 뜰거임.
# 왜냐 이 부분은 수학 상식이 필요하다.나머지를 다 계산한 후에 한번에 구하지말고 나눌때 바로 바로 구해야함.
# https://velog.io/@gidskql6671/나머지Modulo-연산-분배법칙 나머지 정리 참고
# import sys
# a,b,c=map(int, sys.stdin.readline().split())

# def main(a,b,c):
#   result =multiple(a,b)
#   print(result%c)
#   # print(result)
  
# def multiple(a,b):
#   if b==1:
#     return a
#   elif (b%2 == 0): #b가 짝수이면?
#       return multiple(a,b//2)*multiple(a,b//2)
#   else: #홀수이면?
#       return multiple(a,(b//2))*multiple(a,(b//2))*multiple(a,(b%2))
#     # return multiple(a, b-1) * a 

# main(a,b,c)




# 나머지 정리까지 활용했으나.. 그래도 시간초과네..ㅠㅠ b2에 다른 사람 풀이 가져와서 봐볼게
import sys
a,b,c=map(int, sys.stdin.readline().split())

def main(a,b,c):
  result =(multiple(a,b,c))%c
  print(result)
  # print(result)
  
def multiple(a,b,c):
  if b==1:
    return a%c
  elif (b%2 == 0): #b가 짝수이면?
      return ((multiple(a,b//2,c)) * (multiple(a,b//2,c)))%c
  else: #홀수이면?
      return (multiple(a,(b//2),c) * multiple(a,(b//2),c) * multiple(a,(b%2),c))%c
    # return multiple(a, b-1) * a

main(a,b,c)