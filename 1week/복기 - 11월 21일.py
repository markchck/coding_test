# join을 사용하기 sort를 사용하기
# 입력시 sys.stdin.readline()
# 출력시 sys.stdout.write(str(i))

import sys
a = int(input())

num = []

for _ in range(a):
    num.append(int(sys.stdin.readline()))

for i in sorted(num):
    print(i)



