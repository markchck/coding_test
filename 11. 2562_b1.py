# https://www.acmicpc.net/problem/2562


List = []
for i in range(9):
  List.append(int(input()))
max = max(List)
print(max)

for i in range(len(List)):
  if(List[i] == max):
    print(i+1)

