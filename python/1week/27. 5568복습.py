# # 이 문제 딱봐도 노다진데?
# from itertools import permutations
# n,k = int(input()),int(input())
# cards = [ int(input().rstrip) for _ in range(n)]

# 1. 순열로 푸는 방법
from itertools import permutations
N,K=int(input()), int(input())

numbers =[]
for _ in range(N):
    numbers.append(int(input()))
set = set()

for i in permutations(numbers, K):
    #12,3 이랑 1,23 이랑 문제 상황에서는 같다고 보고 싶은데
    #숫자로 놔두면 다른걸로 보이니까 join으로 문자열로 바꿔서 set에 넣는 것.
    set.add(''.join(map(str,i)))
    # set.add((i))
print(len(set))






