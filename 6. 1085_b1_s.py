# https://www.acmicpc.net/problem/1085
x, y, w, h  = map(int, input().split(" "))

n = abs(w-x)
e = abs(h-y)
s = abs(y-0)
w = abs(x-0)

print(min(n,e,s,w))




# # 완전 개 삽 질. 코드는 위에서 아래로 읽히기 때문에 n>e이기만 하면 바로 print(e)가 출력되고 끝나버림...
# x, y, w, h  = map(int, input().split(" "))

# n = abs(w-x)
# e = abs(h-y)
# s = abs(y-0)
# w = abs(x-0)

# if (n>=e):
#   print(1)
#   print(e)
# elif(n>s):
#   print(2)
#   print(s)
# elif(n>w):
#   print(3)
#   print(w)
# elif(e>s):
#   print(4)
#   print(s)
# elif(e>w):
#   print(5)
#   print(w)
# else:
#   print(6)
#   print(w)