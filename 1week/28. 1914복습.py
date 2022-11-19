# n = int(input())

# def recursion(n,a,b,c):
#     if n ==1:
#         print(a,c)
#         return
#     else:
#         recursion(n-1,a,c,b)
#         print(a,c)
#         recursion(n-1, b,a,c)
# if n <= 20:
#     recursion(n,1,2,3)


n= int(input())
count = 0
def recursion(n, a, b, c):
    # global count
    
    #중단조건 n==1일 때
        # 중단조건이면 뭘해? 1에서 3으로 옮겨를 찍어
    #재귀 n!= 1 일 때
        # B구역에서 반복할 건 없고 바로 재귀로 진입
        # n-1개를 첫번째에서 두번째 막대기로 옮겨놓고
        # 첫번재에 가장 밑에 있는 애를 세번째로 옮기고
        # 두번재에 있는 n-1개를 세번째로 옮기면 됨
    if n ==1:
        print(a, c)
        # count+=1
    else:
        recursion(n-1, a, c, b)
        print(a, c)
        # count+=1
        recursion(n-1, b, a, c)
    # return count

print(2**(n)-1) 
if n<=20:
    recursion(n,1,2,3)
# print(count)


