# 중복을 없애는 방법 : set
# 순열, 조합 불러오는 법 : from itertools import permutations 또는 combinations
# join으로 문자를 이어 붙이는 방법 
# map으로 여러 변수를 한번에 형변환 하는 방법

from itertools import permutations

N, K = int(input()), int(input())

numbers = []
for _ in range(N):
    numbers.append( int(input()) )

result=set()
for str_number in permutations(numbers, K):
    result.add(''.join(map(str, str_number)))
print(len(result))

