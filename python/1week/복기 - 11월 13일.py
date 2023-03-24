N=int(input())
count=0
def recursion(n, a,b,c):
    global count
    #중단조건
    if(n==1):
        #A구역
        print(a,c)

    else: #재귀
        #B구역은 없음
        #재귀
        recursion(n-1,a,c,b)
        print(1,3)
        recursion(n-1,b,a,c)
        
if N<=20:
    recursion(N,1,2,3)
