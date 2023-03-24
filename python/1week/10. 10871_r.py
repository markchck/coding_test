# https://www.acmicpc.net/problem/10871

N, X= map(int, input().split(" "))

A = list(map(int, input().split()))
# append.list로 찔러넣기 안됨

for i in A:
  if i < X:
    # print(i, end=' ')
    print(i, end=' ')

# for i in range(N):
#   A.append(int(input()))
