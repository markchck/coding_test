# https://velog.io/@hygge/Python-백준-8983-사냥꾼-Binary-Search
# bisect 내장함수 :https://blog.naver.com/apatocin4869/222684210262
# filter 내장함수 : https://blog.naver.com/ivecoding/222744656718

import sys
from bisect import bisect_left

input = sys.stdin.readline

m,n,l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()
count = 0
for _ in range(n):
    x,y = map(int, input().split())
    position = bisect_left(shoot, x)
    left = abs(x - shoot[position-1])
    
    if position != (m-1):
        right = (abs(x - shoot[position]) + y)
        if(( left+ y)<= l) or ((right +y) <= l):
            count+=1
    else:
        if(left + y) <= l:
            count+=1
print(count)