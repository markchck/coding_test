# https://www.acmicpc.net/problem/5568
# 콤비네이션 하고 4C2  뭘 더 해줘야하는데?
# 실패~~
N= int(input())
K= int(input())

cards=[]
for _ in range(N):
    cards.append(int(input()))

# 2장을 선택
# 뭐가 재귀지...?
def recursion(count):
    #종료조건
        # A구역
    #재귀조건
        # B구역
        # 재귀(증가, 감소)
        # C구역
    if count==K:
        pass
    else:
        # B구역
        recursion(count+1)
        # C구역

# recursion은 N장 중에서 K장으로 만들 수 있는에 숫자를 뱉는 함수이다.
recursion(0)

