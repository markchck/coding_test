# permutation 함수 쓰는 법
# combination 함수 쓰는 법
# 중복된 데이터를 없애기 위한 자료구조 set

from itertools import permutations
from itertools import combinations

a = (set(permutations(range(3),2)))
b = (list(permutations(range(3),3)))

# 얜 어차피 set형태임!
c= (list(combinations(range(3),2)))

# print(a,b)
print(a,b,c)