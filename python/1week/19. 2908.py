# https://www.acmicpc.net/problem/2908
def change(a):
  c = (a[2])
  a[2] = a[0]
  a[0] = c

def list_to_string(a):
  result=''
  for i in range(3):
    result = result + a[i]
  return result

a, b = input().split(" ")
a= list(a)
b= list(b)
change(a)
change(b)
changed_a= int(list_to_string(a))
changed_b= int(list_to_string(b))

if (changed_a> changed_b):
  print(changed_a)
else:
  print(changed_b)



