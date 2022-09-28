# https://www.acmicpc.net/problem/9020
# 이거 유나님의 풀이긴 한데 나주엥 너도 똑같이 풀어봐야해
# 제곱근까지만 소수찾으면된다는 이론으로 푼 것. ex3^2인 9가 소수인지 판단하려면 제곱근인 3까지만 9를 나눠보면 됨. 
# 2로나뉘는지 보고, 3으로 나뉘는지 보고. 
import sys
T = int(sys.stdin.readline())
arr = []
for i in range(T):
    arr.append(int(sys.stdin.readline().strip('\n')))
#arr.sort()
sosu = []
def is_prime(num):
    if num < 2 :
        return False
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            return False
    return True
for i in range(T):
    a = arr[i] // 2
    b = arr[i] // 2
    for j in range(arr[i]):
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a = a - 1
            b = b + 1