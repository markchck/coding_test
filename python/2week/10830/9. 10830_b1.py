# https://www.acmicpc.net/problem/10830
import sys

def involution(input_list, B):
    if B==1:
        return input_list

    tmp=involution(input_list, B//2) #재귀 몫을 구하기 때문에 홀짝에 관계없이 4도 2고 5도 2이다

    if B%2!=0: #홀수이면
        return multiply(multiply(tmp, tmp), input_list)
    else:
        return multiply(tmp, tmp)

def multiply(A, B):
    global N
    result=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j]+=A[i][k]*B[k][j]
            result[i][j]%=1000
    return result



input = sys.stdin.readline

N, B = map(int, input().split())
input_list=[list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        input_list[i][j]%=1000

ans = involution(input_list, B)
for a in ans:
    print(*a)

    



