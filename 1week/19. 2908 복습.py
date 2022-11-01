# 입력값을 split으로 쪼개고
# 첫번째 두번째 배열 값을 구분하고
# 각 배열 숫자들의 순서를 바꿈.
# 그리고 int로 바꿔서 대소비교

# a,b = input().split()
# a= a[::-1]
# b =b[::-1]
# print(max(a,b))


a,b =  input().split()
a= a[: : -1]
b= b[: : -1]
print(max(a,b))


# import sys
# input = sys.stdin.readline
# A, B = input().split()
# A = int(A[2] + A[1] + A[0])
# B = int(B[2] + B[1] + B[0])
# if A>B:
#   print(A)
# else:
#   print(B)