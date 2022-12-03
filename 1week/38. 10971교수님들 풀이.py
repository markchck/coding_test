# https://github.com/jnl1128/W01_teamB8/blob/master/B10971/B10971_pgj.py
from itertools import permutations

n = int(input())
arr = []
matrix = [list(map(int,input().split())) for _ in range(n)]


answer = 10000000 #최초 값을 위한 정수
for i in permutations(range(1,n),n-1):
    num_list = [*i]
    num_list = [0] + num_list + [0] #처음과 끝에 1번도시를 넣어준디
    sub = 0
    
    # for else 구문을 사용하여 경로가 없을 때를 제외한다
    for j in range(n) :
        cost = matrix[num_list[j]-1][num_list[j+1]-1]
        if cost == 0 : ##경로가 없을경우 => 멈춤
            break
        else :
            sub += cost
    	
        # 이미 sub가 answer 이상이면 반복문을 멈춘다
        if sub > answer :
            break
            
    else:
        if answer > sub:
            answer = sub


print(answer)