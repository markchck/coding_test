# 내코드 뭔가 이상함.
def a(n):
  if (n == 0):
    return ("")
  a(n-1)
  for i in range(n):
    print("#"*(i+1))
print(a(2))


# 종우님 코드
# def a(n):
#   if (n == 0):
#     return ("")
#   a(n-1)
#   print("#"*n)
# a(2)