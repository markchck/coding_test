# for문으로 

N = int(input())
def factorial(n):
    for i in range(1, n+1):
        result = result * i
print(factorial(N))



# # 40ms 재귀사용시
# import sys 
# input = sys.stdin.readline
# N=int(input())

# def factorial(n):
#   if n<=1:
#     return 1
#   else:
#     return n*factorial(n-1)

# print(factorial(N))




# A=int(input())


# def multi(a):
#   if a == 0:
#     return 1
#   else:
#     return multi(a-1)*a

# print(multi(A))