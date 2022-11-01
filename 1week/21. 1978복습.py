# 소수 구하는 아리스토의 체 국밥
# # 이 풀이로 외우는게 더 활용도가 높아보임.
n = int(input())
n_list = list(map(int, input().split()))
prime = []
for n in n_list:
    if n!=1:
        for i in range(2,n):
            if n % i ==0:
                break
        prime.append(n)
print(prime)

# n = int(input())
# numbers = map(int, input().split())

# prime=[]
# sosu = 0
# for num in numbers:
#     error= 0 
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 error += 1
#                 break
#         if error == 0:
#             prime.append(num)
# print(len(prime))


