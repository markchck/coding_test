import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
items = []

for i, operator in enumerate(operators):
    if operator != 0:
        for o in range(operator):
            if i == 0:
                items.append('+')
            elif i == 1:
                items.append('-')
            elif i == 2:
                items.append('*')
            elif i == 3:
                items.append('/')

mx = -sys.maxsize
mn = sys.maxsize
for case in list(set(permutations(items))):
    case = deque(case)
    sum = numbers[0]
    for i in range(1, N):
        operator = case.popleft()
        if operator[0] == '+':
            sum += numbers[i]
        elif operator[0] == '-':
            sum -= numbers[i]
        elif operator[0] == '*':
            sum *= numbers[i]
        elif operator[0] == '/':
            if sum >= 0:
                sum //= numbers[i]
            else:
                sum = - (abs(sum) // numbers[i])
    mx = max(mx, sum)
    mn = min(mn, sum)
print(mx)
print(mn)
