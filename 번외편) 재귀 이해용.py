def a(n):
  if (n == 0):
    return ("")
  a(n-1)
  for i in range(n):
    print("#"*(i+1))
print(a(2))

# def a(n):
#   if (n == 0):
#     return ("")
#   a(n-1)
#   print("#"*n)
# a(2)