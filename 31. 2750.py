# https://www.acmicpc.net/problem/2750
# def divide_sort(number_list): #분할정렬(divide_sort)
#   n = len(number_list)
#   if n == 1:
#     return number_list
#   else:
#     # 분할하는 알고리즘 수행
#     mid = n//2
#     left_list = divide_sort(number_list[:mid])
#     right_list = divide_sort(number_list[mid:])

#     # 정렬하는 부분
#     new_list = []
#     if left_list[0] > right_list[0]:
#       new_list.append(right_list[0])
#       new_list.append(left_list[0])
#     else:
#       new_list.append(left_list[0])
#       new_list.append(right_list[0])
#     # (정렬된 숫자를 가진 배열을) 병합하는 알고리즘 수행

#   print(new_list)
#   return new_list

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

N = int(input())
number_list=[]
for i in range(N):
  number = input()
  number_list.append(number)
print(merge_sort(number_list))