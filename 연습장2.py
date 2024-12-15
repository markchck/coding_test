import sys
input = sys.stdin.readline
N = int(input())
list = list(map(int, input().split()))
stack = []
answer = [0] * N
for i in range(len(list)):
    while stack:
        if (list[stack[-1]-1] >= list[i]):  # 왕고가 바뀌지 않는 경우
            answer[i] = stack[-1]
            break
        else:
            stack.pop()
    stack.append(i+1)
print(*answer)
