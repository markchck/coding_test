# https://www.acmicpc.net/problem/2562


List = []
for i in range(9):
  List.append(int(input()))
max = max(List)
print(max)
print(List.index(max)+1)


