# 내 최초 풀이법
# 8시 40분에 시작
# 10시에 답볼게 20분만 더..
# 병합정렬처럼 모든 리스트를 재귀활용해서 반반씩 쪼개서 왼쪽 배열, 오른쪽 배열로 만들고
# 입력값과 대소 비교해서 작으면 왼쪽배열로 가고 크면 오른쪽 배열로 가서 최종 배열의길이가 1일때 입력값과 같으면 1을 출력하고 다르면 0을 출력하는 방식으로 하려햇음. 
# 벗.. 실패(1시간 초과)

# N = int(input())
# A_list = sorted(list(map(int, input().split(" "))))
# M = int(input())
# B_list = list(map(int, input().split(" ")))

# def half(itr_m, A_list):
#   if(len(A_list) == 1):
#     if A_list[0] == itr_m:
#       return 1
#     else:
#       return 0
#   else:
#     mid = A_list[len(A_list)//2]
#     if mid>itr_m:
#       left_A = A_list[:mid]
#       half(itr_m, left_A)
#     elif(mid<itr_m):
#       right_A = A_list[mid:]
#       half(itr_m, right_A)
#     else:
#       return 1

# for itr_m in range(M):
#   half(itr_m, A_list)
