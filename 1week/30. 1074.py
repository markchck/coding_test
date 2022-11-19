# https://www.acmicpc.net/problem/1074
# https://codingcocoon.tistory.com/151
# https://velog.io/@jajubal/파이썬백준-1074-Z ->원리를 이해하는데 도움되지만 시간 초과
# import sys

# result = 0

# def z(n,x,y):
#     global result


# N,r,c = map(int, sys.stdin.readline().split())
# z(2**N, 0, 0)


# 시간초과 뜨는 풀이긴 함.(이해하는데는 더 좋은 ㄷ듯)

def div_con(start_r, start_c, size):
    global cnt
    if size == 2:
        if start_r == r and start_c == c: # 2사분면
            print(cnt)
            return
        cnt += 1
        if start_r == r and start_c + 1 == c: # 1사분면
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c == c: # 3사분면
            print(cnt)
            return
        cnt += 1
        if start_r + 1 == r and start_c + 1 == c: # 4사분면
            print(cnt)
            return
        cnt += 1
    else:
        size //= 2
        div_con(start_r, start_c, size) # 2사분면
        div_con(start_r, start_c + size, size) # 1사분면
        div_con(start_r + size, start_c, size) # 3사분면
        div_con(start_r + size, start_c + size, size) # 4사분면

N, r, c = map(int, input().split())
cnt = 0

div_con(0, 0, 2 ** N)