# https://myjamong.tistory.com/317
# 1차원 배열 풀이인데 넘 어렵다.. 이해못함.
import sys
input = sys.stdin.readline
first, second = input().strip(), input().strip()
len_first, len_second = len(first), len(second)
result = [0] * len_second

for i in range(len_first):
    cnt = 0
    for j in range(len_second):
        if cnt < result[j]:
            cnt = result[j]
        elif first[i] == second[j] :
            result[j] = cnt + 1
print(max(result))

# import sys
# input = sys.stdin.readline
# first = input().strip()
# second = input().strip()
# len_first, len_second=len(first), len(second)
# result = [0]*max(len_first, len_second)

# for i in range(len_first):
#     for j in range(i, len_second):
#         if first[i] == second[j] and first[i] not in second[i:j]:
#             # result[j] += 1 
#             result[j] = max(result) + 1
#         else:
#             result[j] = max(result)
# print(max(result))
