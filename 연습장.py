import sys
input = sys.stdin.readline
N, K = map(int, input().split())
items = str(input().strip())
items = list(items)
stack = []
count = 0
for i, item in enumerate(items):
    while stack and count != K:
        lastItem = stack[-1]
        if item > lastItem:
            stack.pop()
            count += 1
        else:
            break
    stack.append(item)
print(stack)
if len(stack) != N-K:
    for i in range(K):
        stack.pop()
# while len(stack) > N-K:
#     stack.pop()
print(''.join(stack))
