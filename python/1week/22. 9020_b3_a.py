def is_prime(num):
    if num == 1:
        return False
    for n in range(2, int(num**0.5)+1):
        if num % n ==0:
            return False
    else:
        return True

for _ in range(int(input())):
    num = int(input())
    a,b  = num//2, num//2
    while a>0:
        if is_prime(a) and is_prime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1
        

