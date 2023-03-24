from itertools import permutations


n = int(input())
arr = []

matrix = [list(map(int,input().split())) for _ in range(n)]

answer = 100000000  

# print(list(permutations(range(1,n), n-1)))
for i in permutations(range(1,n), n-1):
    # num_list =[]
    # num_list.append(list(i))
    num_list = [*i]
    num_list = [0] + num_list + [0]
    sub = 0

    for j in range(n):
        cost = matrix[num_list[j]-1][num_list[j+1]-1]
        if cost == 0:
            break
        else:
            sub = sub + cost
print(sub)
    
    
    
