# https://www.acmicpc.net/problem/1085
x, y, w, h  = map(int, input().split(" "))

n = abs(w-x)
e = abs(h-y)
s = abs(y-0)
w = abs(x-0)

# x의 최대 길이가 1000이라는 점에 착안해서 nesw가 1000-n이 가장 작은 놈?