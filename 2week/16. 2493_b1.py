import sys
from collections import deque
deq= deque

N=int(input())
deq=deq(map(int, sys.stdin.readline().split()))
count =0
# print(deq)
# print(len(deq))

for i in range(len(deq)-1,-1,-1):
    for j in range(len(deq)-2,-1,-1):
        if deq(i)<deq(j): #뒤에 있는 타워가 키가 더 큰 더 뒤에있는 타워를 만나면..
            count+=1
            break
        else:
            print(f"가장 키큰 타워는 {i}")