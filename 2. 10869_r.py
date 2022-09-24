# https://www.acmicpc.net/problem/10869
# 두 자연수 a와 b가 주어진다. 이때, a+b, a-b, a*b, a/b(몫), a%b(나머지)를 출력하는 프로그램을 작성하시오. 
a, b = map(int, input().split(" "))
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)


# # 오답(a,b를 한번에 입력받으라했지 따로 따로 받으라고 안했음)
# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)