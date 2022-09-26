# 유나님의 코드인데 
# 1. 제곱근을 활용한 빠르게 소수 판별하는 거 적용
# 2. 차이값 적은거 반환하는 함수 반띵해서 input값이랑 같으면 바로 print하고 아니면 앞에 자리는 -1, 뒤에자리는 +1하는 식으로 구현.

# https://blog.naver.com/nuang0530/222865433145 왜 소수를 판별할 때는 제곱근까지만 보면 되는가? 설명 잘 나와있음.


# import sys
# T = int(sys.stdin.readline())
# arr = []
# for i in range(T):
#     arr.append(int(sys.stdin.readline().strip('\n')))
# #arr.sort()

# sosu = []
# def is_prime(num):
#     if num < 2 :
#         return False
#     for j in range(2, int(num ** 0.5) + 1):
#         if num % j == 0:
#             return False
#     return True

# for i in range(T):
#     a = arr[i] // 2
#     b = arr[i] // 2
#     for j in range(arr[i]):
#         if is_prime(a) and is_prime(b):
#             print(a, b)
#             break
#         else:
#             a = a - 1
#             b = b + 1