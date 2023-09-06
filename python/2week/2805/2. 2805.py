# https://www.acmicpc.net/problem/2805
# 3 2
# 3 3 3
# 2가 나와야함


N, M = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))
start, end = 0, max(trees)

while start <= end:
    mid = (start+end)//2
    tree = 0  # 잘린 나무 합
    for i in trees:
        if i > mid:
            tree = tree + i - mid
    if tree >= M:
        start = mid+1
    else:
        end = mid-1
print(end)
