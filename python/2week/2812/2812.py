import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = list((map(int, input().strip())))
k, stack = K, []

for i in range(N):
    while (k > 0 and stack and stack[-1] < items[i]):
        stack.pop()
        k -= 1
    stack.append(items[i])

print("".join(map(str, stack[: N-K])))
