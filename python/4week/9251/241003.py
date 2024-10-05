# 시간이 O(n!) 0.1초라 완전탐색으론 절대 안됨. (DP같이 매우 효율적인 방식을 써야함.)
#  -> 잘못생각함 n2이고 2초니까 최악의 경우가 1억이고 따라서 시간복잡도 신경 덜 써도 된다.

# 메모를하고 + 점화식을 찾는다. 결괏값은 메모[n]번째 인자를 출력하는 방식
# Sn = S(n-1) +1(for문으로 나머지 문자열 찾기) 점화식


import sys
input = sys.stdin.readline
first = input().strip()
second = input().strip()
len_first = len(first)
len_second = len(second)
result = [[0]*(len_second+1) for _ in range(len_first+1)]

for i in range(1, len_first+1):
    for j in range(1, len_second+1):
        if (first[i-1] == second[j-1]):
            result[i][j] = result[i-1][j-1] + 1
        else:
            result[i][j] = max(result[i-1][j], result[i][j-1])
print(result[-1][-1])
