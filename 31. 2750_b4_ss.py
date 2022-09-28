# https://www.acmicpc.net/problem/2750

# 병합정렬 풀의법 (시간복잡도 n*logn )

#arr[:mid] -> 배열 슬라이싱을 활용해서 이렇게 단순하게 배열 반띵하기 완료. 
#난 어케할라그랫냐면 len으로 배열의 길이 n을 구하고, n을 반으로 나누고 그걸 m(mid)이라하고(홀수일때를 대비해서 round처리)
#for문을 돌면서 0~m-1까지를 새로운 배열 left라 하고
#m~n까지를 또 포문 돌려서 이터레이팅하고 새로운 배열 right라 하려고 했음.
#그리고 left배열을 merge_sort(left) 인자로 넣고, right배열을 (right)인자로 넣고 재귀를 돌린다.
#틀린건 아닌데 코드 길어지는거 생각해봐 ㅋㅋ그냥 arr[:m]이게 끝낼 수 있는건데..


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    merged_arr = []
    len_l=len(left_arr)
    len_r=len(right_arr)

    tmp_a = 0
    tmp_b = 0
    tmp_c = 0
    # if (tmp_a < len_l and tmp_b < len_r):
    while ((tmp_a < len_l) and (tmp_b < len_r)): 
      
      if (left_arr[tmp_a] < right_arr[tmp_b]):
        merged_arr.append(left_arr[tmp_a])
        tmp_a = tmp_a + 1
      else:
        merged_arr.append(right_arr[tmp_b])
        tmp_b = tmp_b + 1
      tmp_c = tmp_c + 1
    else:
    # 배열이 길이가 달라서 남게되는 짜투리 merged_arr에 합치는 과정
      while tmp_a<len_l:
        merged_arr.append(left_arr[tmp_a])
        tmp_a = tmp_a + 1
        tmp_c = tmp_c + 1
      
      while tmp_b<len_r:
        merged_arr.append(right_arr[tmp_b])
        tmp_b = tmp_b + 1
        tmp_c = tmp_c + 1

      # # # merged_arr.append(left_arr[tmp_a: ]) #이렇게하면 배열안에 배열이 들어가게 되어 배열과 int는 대소를 비교할 수 없다는 에러 뜸.
      # # # 파이썬은 배열끼리 +가 된다는 점을 이용하면 이렇게도 가능 
      # merged_arr = merged_arr + left_arr[tmp_a: ]
      # merged_arr = merged_arr + right_arr[tmp_b: ]
      
    return merged_arr


N = int(input())
number_list=[]
for i in range(N):
  number = int(input())
  number_list.append(number)
print(merge_sort(number_list))