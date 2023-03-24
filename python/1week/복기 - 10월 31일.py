# 소수판별하는 국밥 쓰기
n = int(input())
n_list = map(int, input().split())

prime = []
for n in n_list:
    if n>1:
        for i in range(2, n):
            if i % n ==0:
                break
        prime.append(n)
print(prime)