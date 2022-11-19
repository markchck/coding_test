import sys
count = 0

def z(n,x,y):
  global count

  if not(x <= r < x+n and y <= c <y+n):
    count += n**2
    return

  if x == r and y ==c:
    print(int(count))
    return

  else:
    z(n / 2, x, y)
    z(n / 2, x, y + n / 2)
    z(n / 2, x + n / 2, y)
    z(n / 2, x + n / 2, y + n / 2)

n, r, c = map(int, sys.stdin.readline().split(' '))
z(2 ** n, 0, 0)