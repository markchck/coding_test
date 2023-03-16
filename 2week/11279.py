from heapq import heappush, heappop, heapify, heappushpop, heapreplace
import sys 
input = sys.stdin.readline
N = int(input())
list_a =[]


for i in range(N):
    number=int(input())
    if number ==0:
        if list_a:
            print(heappop(list_a)[1])
        else:
            print(0)
    else:
        heappush(list_a, (-number, number))
