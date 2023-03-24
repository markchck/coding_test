# https://www.acmicpc.net/problem/8983
# 왐마!!!!!!!!!!내가 풀었는데 100점나옴!!!!!!!!!!!
# 첨엔 못풀었고, 해설을 보는데 동물을 기준으로 봐야한다는 힌트를 참고해서 내가 구현해봄.
# 첨엔 9점이었는데 런타임 에러가 떴음. 런타임 에러는 배열의 인덱스를 잘못 참조했을 때 또는 0으로 나눈다거나 논리적으로 말이 안 될 때 발생
# 동물이 맨 오른쪽 사대에 위치하는 경우 예외 케이스 핸들링해서 돌렸더니 100점!!!

# 동물이랑 가장 가까운 사로구할 때 이진탐색이 들어가는데 이걸 bisect라는 내장함수를 쓰면 나처럼 binary함수 안돌려도 인덱스 바로 구해준다니까
# 내일은 bisect함수 사용해보자

import sys
input = sys.stdin.readline

#사대, 동물, 사정거리
m,n,l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()

def binary(x):
    left = 0
    right = (m-1)
    res = 0
    while(left <= right):
        mid = (left+right)//2
        if x >= shoot[mid]:
            res = mid
            left = mid + 1
        else:
            right = mid-1 
    return res

def boj8983():
    count = 0
    for _ in range(n):
        x, y = map(int, input().split())
        index = binary(x)
        if index != (m-1): #동물이 두 사대 사이에 위치한 경우
            if (abs(shoot[index] - x) + y <= l) or (abs(shoot[index+1] - x ) + y <= l): #사정거리 안이라면?
                
                count +=1
        else: #동물이 하필 맨 끝 사대의 오른쪽에 있는 경우
            if (abs(shoot[index] - x) + y <= l):
                count +=1
    return count

print(boj8983())