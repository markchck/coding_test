# 골디바흐 풀이전체 암기 테스트
def is_prime(number):
    if number == 1:
        return False
    for num in range(2, int(number**0.5)+1):
        if (number % num ==0):
            return False
    else:
        return True


for _ in range(int(input())):
    n = int(input())
    a,b = n//2, n//2
    while(a>0):
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1