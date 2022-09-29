# https://www.acmicpc.net/problem/2588


# 10으로 나눈 나머지를 활용한 풀이
a= int(input())
b= int(input())

# 3
b0 = b//100
# 8
b1 = (b//10)%10
# 5
b2 = (b%100)%10

c= a*b2
d= a*b1
e= a*b0
f= c + d*10 + e*100
print(c,d,e,f, sep='\n')


