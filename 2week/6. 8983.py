# https://www.acmicpc.net/problem/8983
# bisect 내장함수 :https://blog.naver.com/apatocin4869/222684210262
# filter 내장함수 : https://blog.naver.com/ivecoding/222744656718
import sys
from bisect import bisect_left
input = sys.stdin.readline

# m: 사로의 수, n: 동물의 수, l: 사정거리
m,n,l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()

cnt = 0
for _ in range(n):
    x,y = map(int, input().split())
    if y <= l: #y가 l 보다 큰 경우는 맞출수가 없다.
        idx = bisect_left(shoot, x)
        for k in [idx-1, idx, idx+1]: