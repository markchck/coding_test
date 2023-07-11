import sys
input = sys.stdin.readline
N = int(input())
items = []
for _ in range(N):
    start, end = map(int, input().split(' '))
    items.append((start, end))

items.sort(key=lambda x: (x[1], x[0]))

count = 0
while items:
    start, end = items[0]
    items = items[1:]
    count += 1
    for i, item in enumerate(items):
        nStart, nEnd = item[0], item[1]
        if (nStart >= end):
            items = items[i:]
            break
    else:
        break
print(count)
