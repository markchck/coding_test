list_l = []

for _ in range(9):
  list_l.append(int(input()))

# list_l.sort()
# print(list_l)

from itertools import combinations

com_list_l = (combinations(list_l, 7))
child=[]
for com in com_list_l:
  if sum(com) ==100:
    child=list(com)
    # print(child)
    # print(child.sort())
child=sorted(child)

for i in child:
  print(i)

