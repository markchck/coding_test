# 1.count함수의 활용
# 2.입력과 동시에 곱하는 방식

a=str(int(input())*int(input())*int(input()))
for i in range(10):
    print(a.count(str(i)))