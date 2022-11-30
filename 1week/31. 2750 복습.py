# N = int(input())
# list_l = []
# for _ in range(N):
#     list_l.append(int(input()))


# a=sorted(list_l)

# for _ in a:
#     print(_)


import sys
n= int(sys.stdin.readline())
l=[]

for i in range(n):
    l.append(int(sys.stdin.readline()))

l.sort()

# print(' '.join(map(str, l)))

for i in range(len(l), 0 -1):
    print(i)

