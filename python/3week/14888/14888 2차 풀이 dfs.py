# nxnxnxn경우의 수로 끝내려면 백트래킹 사용하면 됨. dfs로 탐색하고 N이 되면 멈추고 백트래킹 쉽게 최대한 매개변수에 넣자
import sys
N = int(input())
numbers = list(map(int, input().split()))
add, minus, multi, divide = map(int, input().split())


def dfs(add, minus, multi, divide, sum, idx):
    global mx, mn
    if idx == N:
        mx = max(mx, sum)
        mn = min(mn, sum)
        return
    else:
        if add > 0:
            dfs(add-1, minus, multi, divide, sum + numbers[idx], idx + 1)
        if minus > 0:
            dfs(add, minus-1, multi, divide, sum - numbers[idx], idx + 1)
        if multi > 0:
            dfs(add, minus, multi-1, divide, sum * numbers[idx], idx + 1)
        if divide > 0:
            if sum >= 0:
                dfs(add, minus, multi, divide-1, sum // numbers[idx], idx + 1)
            else:
                dfs(add, minus, multi, divide-1,
                    (abs(sum) // numbers[idx])*-1, idx + 1)


mx = -sys.maxsize
mn = sys.maxsize

dfs(add, minus, multi, divide, numbers[0], 1)
print(mx)
print(mn)
