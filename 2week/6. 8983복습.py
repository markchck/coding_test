# https://velog.io/@hygge/Python-백준-8983-사냥꾼-Binary-Search
# bisect 내장함수 :https://blog.naver.com/apatocin4869/222684210262
#   정렬된 배열의 몇번 째 인덱스에 그 데이터를 넣으면 배열이 정렬된 상태를 유지하는 가를 알려준다.
#   bisect(배열, 넣을 숫자)
# 
# import bisect
# a = [1, 3, 5, 7, 9]
# print(bisect.bisect(a,2))
# >>1   #2는 1과 3사이 즉 a[1]에 삽입되면 a가 정렬상태를 유지한다. 따라서 1을 리턴한다
#  근데 bisect.bisect(a,2) 이 아니라 bisect.bisect(a,3) 이었다면

# 1과 3사이 혹은 3과 5사이중 어디에 들어갔을 거라고 bisect는 판단 할 것인가?
# 이는 bisect의 메서드 bisect, bisect_left, bisect_right가 판단을 달리한다.
# 1. bisect, bisect_right (둘은 항상 같은 값을 반환한다. 이름만 다르고 같은 메서드다)
#      3과 5사이라고 생각한다

# filter 내장함수 : https://blog.naver.com/ivecoding/222744656718


import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

m,n,l = map(int, input().split())
shoot = list(map(int, input().split()))
shoot.sort()
count = 0
for _ in range(n):
    x,y = map(int, input().split())
    position = bisect_left(shoot, x)
    left = abs(x - shoot[position-1])
    
    if position <= (m-1):
        right = (abs(x - shoot[position]))
        #버그...이렇게 써서 계속 3이나오는거였음.. right = (abs(x - shoot[position])+y)
        if(( left+ y)<= l) or ((right +y) <= l):
            count+=1
    else:
        if(left + y) <= l:
            count+=1
print(count)