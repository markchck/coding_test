# 특정 숫자가 소수인지 판별기
def is_prime(number):
    if number == 1:
        return False
    for n in range(2, int(number **0.5) +1):
        if number % n ==0:
            return False
    else:
        return True

# 여러 숫자들 중 소수 판별기 (제곱근 활용)
def prime_search_1(numbers):
    prime_1=[]
    for num in numbers:
        if num >1:
            for n in range(2, int(num**0.5)+1):
                if num % n ==0:
                    break
            else:
                prime_1.append(num)
    return prime_1

# 여러 숫자들 중 소수 판별기 (제곱근 안 활용)
def prime_search_2(numbers):
    prime_2 = []
    for num in numbers:
        if num > 1:
            for n in range(2, num):
                if num % n ==0:
                    break
            else:
                prime_2.append(num)
    return prime_2

# 특정 숫자까지의 소수를 추출하기 (제곱근 활용)
def range_prime_1(number):
    prime=[]
    for num in range(number):
        if num >1:
            for n in range(2, int(num**0.5) +1 ):
                if num % n ==0:
                    break
            else:
                prime.append(num)
    return prime

# 특정 숫자까지의 소수를 추출하기 (제곱근 안 활용)
def range_prime_2(number):
    prime = []
    for num in range(number):
        if num >1:
            for j in range(2, num):
                if num%j==0:
                    break
            else:
                prime.append(num)
    return prime


# numbers=[1,2,3,4,5,6,7]
# print(is_prime(8))
# print(prime_search_1(numbers))
# print(prime_search_2(numbers))
# print(range_prime_1(100000))
# print(range_prime_2(100000)) #주의 이거 돌리면 함흥차사임


