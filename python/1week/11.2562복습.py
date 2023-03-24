import sys
input = sys.stdin.readline

A=[]
for _ in range(9):
    A.append((int(input())))
# print(A)

highest_n = max(A)
print(highest_n)

for i in range(len(A)):
    if A[i] == highest_n:
        print(i+1)