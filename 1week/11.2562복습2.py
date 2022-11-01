import sys
input = sys.stdin.readline

A=[]
for _ in range(9):
    A.append((int(input())))
# print(A)

highest_n = max(A)
print(highest_n)
print(A.index(highest_n)+1)