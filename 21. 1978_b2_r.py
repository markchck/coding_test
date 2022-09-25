# https://www.acmicpc.net/problem/1978
# https://ooyoung.tistory.com/92 풀이 가져옴 (range(2, num)이 코드 양 많이 줄이네) 근데 왜 오답 뜨냐? 
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
# 1부터 100까지 소수 총 25개 넣으면 25개라고 정답 잘 나오는데.. 뭐지?
n = int(input())
numbers=map(int, input().split(","))
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
  