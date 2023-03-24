# https://www.acmicpc.net/problem/10819
N = int(input())
list_l =map(int, (input().split()))

from itertools import permutations as p 

all_case=list(p(list_l, N))

result = 0
for one_case in all_case:
    part_sum = 0
    for i in range(len(one_case)-1):
        part_sum += abs(one_case[i] - one_case[i+1])
    if part_sum > result:
        result = part_sum
    #     for j in range(i+1, len(one_case)):
    #     # 앞 뒤를 빼게 하는 로직을 어케 구현?
    #         part_sum = abs(one_case[i] - one_case[j])
    #         result.append(part_sum)
    #         break
print(result)
# print(max(result))

# 앞뒤를 빼는 로직
# 합을 누적하는 로직
# 리스트를 안 쓰고 최댓값을 갱신하면서 출력하는 로직