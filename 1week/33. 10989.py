# https://www.acmicpc.net/problem/10989
# # 메모리초과
# import sys
# input = sys.stdin.readline

# list_l = []
# for _ in range(int(input())):
#     list_l.append(int(input()))

# list_l.sort()
# for i in list_l:
#     print(i)


# 개수정렬사용해야함. 
# log*n정렬 알고리즘들은 기본적으로 모든 전표들을 책상에 한 장 씩 펼쳐놓고(분할하고) 합치면서 정렬하는 방식을 사용한다.
# 즉, 공간복잡도를 희생해서 시간복잡도를 줄이는 방식(책상에 전표를 쫙 펼쳐야하니까 - 공간복잡도 증가함)
# 근데 전표정리할 때 (그럴리는 없지만) 동일한 전표가 4개 있다고 쳐봐. 그럼 그걸 책상에 따로 따로 펼쳐놓으면 공간 낭비임. 같은건 뭉쳐놔야지. 
# (단순 정렬알고리즘 쓰면 같은 전표를 전부 펼쳐놓아야하기 때문에 메모리 초과가 발생함.) -> 같은 전표는 뭉치는 알고리즘이 개수정렬 알고리즘이다.
# https://coarmok.tistory.com/entry/파이썬python-백준-10989번-메모리-초과

import sys
input = sys.stdin.readline
N = int(input())
arr = [0] *10001

for i in range(N):
    a = int(input())
    arr[a-1] += 1

# 1차원 배열은 2가지 정보를 담을 수 있다. 
# a[x] = y 하면 x가 y개 있다는 소리
# a[0] = 2 하면 0+1(프로그래머는 0부터 센다)이 2개가 있다

# 이렇게 하면 인덱싱정보에 접근 못해서 못푼다 아래처럼
# 인덱싱정보에 접근할 수 있게 for문돌려야함
# for num in arr:  
#     if num != 0:
#         for n in range(num):
#             print(num)

for i in range(10001):
    if(arr[i] != 0):
        for _ in range(arr[i]):
            print(i+1)