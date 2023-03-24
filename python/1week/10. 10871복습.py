# 입력받고, 오름차순으로 정렬하고 이진탐색으로 ?
a, b= map(int, input().split())
A = list(map(int, input().split()))

for i in A:
    if i < b:
        print(i, end=' ')
