# https://www.acmicpc.net/problem/2588


# input은 문자열을 반환한다는 점을 사용한 이상한 풀이법
a = int(input())
b = input() 
c = int(b[2]) * a 
d = int(b[1]) * a
e = int(b[0]) * a
f = c+10*d+100*e
# print(c)
# print(d)
# print(e)
# print(f)

print(c,d,e,f, sep='\n')