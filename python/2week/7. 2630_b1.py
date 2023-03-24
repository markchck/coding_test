# 7번 색종이 만들기 코드
# 준호 코드

import sys

global w_count, b_count
w_count = 0
b_count = 0

def main() -> None:
    global w_count, b_count
    n = int(sys.stdin.readline().strip())
    arr = [0]*n
    for i in range(n):
        arr[i] = list(map(int, sys.stdin.readline().split()))
    
    is_same(arr, n)
    # n은 종이 모서리의 길이

    print(w_count)
    print(b_count)


def paper_cut(arr, n) -> None:
    global w_count, b_count
    if n == 2:
        # 원소가 통일되지 않은 2x2 배열이 들어온 상태임.
        for row in arr:
            for data in row:
                if data == 0: w_count += 1
                else: b_count += 1
    else:
        part_0 = [[0 for _ in range(n//2)] for _ in range(n//2)]
        part_1 = [[0 for _ in range(n//2)] for _ in range(n//2)]
        part_2 = [[0 for _ in range(n//2)] for _ in range(n//2)]
        part_3 = [[0 for _ in range(n//2)] for _ in range(n//2)]

        for i in range(0, n):
            for j in range(0, n):
                if i/(n//2) < 1 and j/(n//2) < 1:
                    part_0[i%(n//2)][j%(n//2)] = arr[i][j]
                elif i/(n//2) < 1 and j/(n//2) >= 1:
                    part_1[i%(n//2)][j%(n//2)] = arr[i][j]
                elif i/(n//2) >= 1 and j/(n//2) < 1:
                    part_2[i%(n//2)][j%(n//2)] = arr[i][j]
                else:
                    part_3[i%(n//2)][j%(n//2)] = arr[i][j]

        is_same(part_0, n//2)
        is_same(part_1, n//2)
        is_same(part_2, n//2)
        is_same(part_3, n//2)


def is_same(arr, n) -> None:
    global w_count, b_count
    a = arr[0][0]
    same = True

    for row in arr:
        for data in row: 
            if data != a:
                same = False
                break

    if same == True:
        if a == 0:
            w_count += 1
        else:
            b_count += 1
    else:
        paper_cut(arr, n)


main()