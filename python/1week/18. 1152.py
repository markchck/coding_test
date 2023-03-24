# https://www.acmicpc.net/problem/1152

a = input()
A= a.strip()
# print(A.split(" "))
List = A.split(" ")

if (len(List) == 1) and List[0] == '':
  print(len(List)-1)
else:
  print(len(List))

print( '' == None)

# print(ord(" "))
# print(chr(32))
