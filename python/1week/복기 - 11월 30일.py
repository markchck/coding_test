# 경우의 수 노가다는 permutation을 쓰면 편하게 모든 경우의 수가 나오는구나
# 왕복 조건이 있으면 배열 맨 끝에 출발점을 list.append로 넣어줘야하는구나

N = int(input())
from itertools import permutations

list_l=[]
for i in range(N):
    list_l.append(i)

list_l = permutations(list_l,N)

for case in list_l:
    case = list(case)
    # print(case)
    case.append(case[0])
    print(case)