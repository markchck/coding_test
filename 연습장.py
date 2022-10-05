
result=[[0]*2 for _ in range(2)]
for i in range(2):
    for j in range(2):
        for k in range(2):
            result[i][j]+=A[i][k]*B[k][j]
        result[i][j]%=1000
