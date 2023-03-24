# 10819번
# 코드를 짜지 않고도 내 가설을 테스트 해본다는 생각
#     - 최대 최소를 번갈아 쓰면 되지 않을까? 생각했으면 코드부터 짜지말고 테스트 케이스 숫자가지고 암산해서 출력값이랑 같으면 고, 다르면 가설 버리면 됨
# 브루트포스 문제임을 알아채는 게 중요한데 그 사고 과정
#     - 어라? 제약조건에 따르면 기껏해야 8!이네? (노가다 뛰어도 되겠는걸?)
# 앞뒤를 빼는 로직
#     - for (0 ~ n-1) 까지 a[i] - a[i+1] 
# 합을 누적하는 로직
#     - s = s + sum
# 리스트를 안 쓰고 최댓값을 갱신하면서 출력하는 로직
#     - if sum > result 
#         result = sum

N = int(input())
from itertools import permutations
list_l=list(map(int, input().split()))

A = list(permutations(list_l))
result = 0
for a in A:
    sum= 0
    for i in range(len(a)-1):
        sum += abs(a[i]-a[i+1])
    if sum > result:
        result = sum
print(result)

