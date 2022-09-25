# https://www.acmicpc.net/problem/1978
# https://ooyoung.tistory.com/92 풀이 가져옴 (range(2, num)이 코드 양 많이 줄이네)
n = int(input())
numbers=map(int, input().split(" "))
sosu = 0

for num in numbers:
  error = 0
  if num > 1 :
    for i in range(2, num):
      if num % i == 0:
        error = error + 1
    if error == 0:
      sosu = sosu +1
print(sosu)
  