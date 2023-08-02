from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
operations_num = list(map(int, input().split()))
operations_type = ['+', '-', '*', '//']
operations = []

# 쓸 수 있는 연산자의 배열을 어떻게 만들지 ['+', '+', '-', '*', '//']
for i in range(4):
    for _ in range(operations_num[i]):
        operations.append(operations_type[i])

# 모든 연산자 순열을 구한다.
maxnum = -int(1e9)
minnum = int(1e9)
allCase = list(set(permutations(operations, N-1)))

for case in allCase:
    total = numbers[0]
    for i in range(1, N):
        if case[i-1] == '+':
            total += numbers[i]
        elif case[i-1] == '-':
            total -= numbers[i]
        elif case[i-1] == '*':
            total *= numbers[i]
        elif case[i-1] == '//':
            if total < 0:
                total = -(abs(total) // numbers[i])
            else:
                total = total // numbers[i]
    maxnum = max(maxnum, total)
    minnum = min(minnum, total)
print(maxnum)
print(minnum)


# from itertools import permutations
# import sys
# input = sys.stdin.readline
# N = int(input())
# numbers = list(map(int, input().split()))
# operations_num = list(map(int, input().split()))
# operations_type = ['+', '-', '*', '//']
# operations = []

# # 쓸 수 있는 연산자의 배열을 어떻게 만들지 ['+', '+', '-', '*', '//']
# for i in range(4):
#     for _ in range(operations_num[i]):
#         operations.append(operations_type[i])

# # 모든 연산자 순열을 구한다.
# allCase = permutations(operations, len(operations))
# total = numbers[0]
# maxnum = -10**13
# minnum = 10**13
# for case in allCase:
#     # 각 케이스마다 합계를 계산하면 됨
#     for i in range(1, len(numbers)):
#         for operation in case:
#             if operation == '+':
#                 total += numbers[i]
#             elif operation == '-':
#                 total -= numbers[i]
#             elif operation == '*':
#                 total *= numbers[i]
#             elif operation == '//':
#                 if total < 0:
#                     total = -(abs(total) // numbers[i])
#                 else:
#                     total = total // numbers[i]
#     maxnum = max(maxnum, total)
#     minnum = min(minnum, total)
# print(maxnum)
# print(minnum)
