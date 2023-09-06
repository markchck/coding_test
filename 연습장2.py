import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = str(input().strip())
items = list(items)
stack = []
count = 0
k = K
for i, item in enumerate(items):
    while stack and k > 0 and stack[-1] < items[i]:
        stack.pop()
        k -= 1
    stack.append(item)
# if len(stack) != N-K:
#     for i in range(K):
#         stack.pop()
print("".join(map(str, stack[: N-K])))
