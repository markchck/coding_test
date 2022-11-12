# https://www.acmicpc.net/problem/1914
# 현재위치와 옮긴 위치를 어떻게 출력하지?
N = int(input())
num=0
def recursion(count):
    # 중단을 언제?
    if count == 0:
        #한개 밖에 없으면 1에서 3으로 그냥 옮기면 됨.
        num += 1
        print(1,3)
        
    # 재귀도는건 뭐야?
    else:
        recursion(count-1)
        print(num)

recursion(N)
print(num)