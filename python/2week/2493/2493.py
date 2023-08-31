import sys
input = sys.stdin.readline

N = int(input())
items = list(map(int, input().split()))
answer = [0] * len(items)
stack = []
for i in range(N):
    while stack:
        idx = stack[-1]
        if items[i] > items[idx]:
            stack.pop()
        else:
            answer[i] = idx+1
            break
    stack.append(i)
print(*answer)


# import sys
# input = sys.stdin.readline

# N = int(input())
# items = list(map(int, input().split()))
# answer = [0] * len(items)
# for i in range(len(items)-1, -1, -1):
#     for j in range(i-1, -1, -1):
#         if items[j] >= items[i]:
#             answer[i] = j+1
#             break
#     else:
#         answer[i] = 0
# print(answer)
