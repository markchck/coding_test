from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
ans = []
q = deque(i for i in range(1, n+1))
while q:
    for i in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())
print('<', end='')
print(*ans, sep=', ', end='')
print('>')
