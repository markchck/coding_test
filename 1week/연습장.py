# n = int(input())
# numbers = map(int, input().split())

# prime=[]
# for num in numbers:
#     if num >1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         prime.append(num)
# print(prime)

n = int(input())
numbers = map(int, input().split())

prime=[]
for num in numbers:
    if num >1:
        for i in range(2, num):
            if num % i == 0:
                break
        prime.append(num)
print(prime)
