# https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

import sys
input = sys.stdin.readline

A,B,C = map(int, input().split())

def BOJ1629(a,b,c):
    if b== 1:
        return a%c
    else:
        tmp = BOJ1629(a, b//2, c)
        if b%2==0:
            return tmp%c*tmp%c
        else:
            return tmp%c*tmp%c*a%c

print(BOJ1629(A,B,C))



# boj(10,1,12)
# boj(10,2,12) 
# boj(10,5,12) 
# boj(10,11,12) 

이 순서대로 스택이 쌓이고
boj(10,1,12)가 b==1이라서 boj(10,2,12)세계에 tmp = 10을 리턴하고 팝된다. 
boj(10,2,12)세계에서는 b%2==0이기에 10*10을 12로 나눈 나머지 4가 boj(10,5,12)세계에 tmp로 리턴되고 boj(10,2,12)는 팝된다.
boj(10,5,12)세계에서는 b는 홀수이기에 4*4*10을 12로 나눈 나머지 4가 boj(10,11,12)세계에 리턴되고 boj(10,5,12)는 팝된다.
boj(10,11,12)세계에서는 더이상 쌓여있는 스택이 없고(다 팝 됐음) print(4)만 하면 된다.