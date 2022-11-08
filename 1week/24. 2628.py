# https://www.acmicpc.net/problem/2628
# 10 8
# 3
# 0 3 (0, 가로row)
# 1 4 (1, 세로col)
# 0 2
# col쪽에서 가장 긴 놈과 row쪽에서 가장 긴 놈의 곱하기를 해주면 됨.

# 실패(두번째 자르는 경우 생각 못함)
# col, row = map(int, (input().split()))
# cutting_count = int(input())

# for _ in range(cutting_count):
#   cutting_col, cutting_row = map(int, input().split())
#   left_col = col - cutting_col
#   left_row = row - cutting_row
#   max_row = max(left_row ,cutting_row)
#   max_col = max(left_col, cutting_col)
#   print(max_row*max_col)
