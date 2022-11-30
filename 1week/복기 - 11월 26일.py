# 3중 for 문을 돌면서 한장씩 골라서 더하는 로직

n = 5

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            print(i+j+k)