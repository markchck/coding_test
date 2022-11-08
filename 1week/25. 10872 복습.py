A=int(input())


def multi(a):
  if a == 0:
    return 1
  else:
    return multi(a-1)*a

print(multi(A))