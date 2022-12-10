# https://latte-is-horse.tistory.com/316
# 이 풀이가 이진탐색을 사용한다는 점에서 더 의도에 맞다.

import sys
# sys.stdin = open('2407.txt', 'r')
input = sys.stdin.readline


N = int(input())
arr = sorted(list(map(int, input().split())))

def binary_search(idx, target):
    res = N-1
    start, end = idx, N - 1

    while start <= end:
        mid = (start+end) //2
        # if(arr[mid] == target): #나무자르기나 다른곳에서는 나무도 자르면서 환경도 보호하라해서 이렇게 맞는 숫자 나와도 break하면 안되는데 이 문제에서는 맞으면 아무거나 출력하라고 해서 ==target이 나오면 걍 return해도 됨
        #     return mid 
        # elif arr[mid] > target:
        #     end = mid -1
        #     res = mid
        # else:
        #     start = mid +1

        if(arr[mid] >= target): #이렇게 써도 통과~
            res = mid
            end=mid-1
        else:
            start= mid+1
    return res

def solution():
    v1, v2 = 0, 0
    best_sum = 10 ** 10
    for i in range(N):
        # 이분 탐색 수행: 현재 위치(i) 이후의 용액에서 탐색, 찾는 값은 (현재 용액 * -1)
        # 그니까 i번째(3번째) 숫자가 -99라고하면 i+1번째(4번째) 숫자부터 배열의 끝인 n-1까지 뒤지는데 
        # 찾는 숫자는 -(-99) 즉 99를 찾는다는 소리임 
        # 그래야 우리의 목표인 합쳐서 0이 되는 용액을 찾는거니까
        # 우리는 정렬을 이미 했기 때문에 i보다 왼쪽에 있는 숫자들(0,1,2)은 안봐도 됨 i가 -99면
        # 걔네들은 -120, -110 이라 더하면 0에 가까워지는게 아니라 더 멀어지는 놈들이니까
        res = binary_search(i + 1, -arr[i])
        
        # 찾은 용액의 왼쪽 용액 확인
        if i + 1 <= res - 1 < N and abs(arr[i] + arr[res - 1]) < best_sum:
            best_sum = abs(arr[i] + arr[res - 1])
            v1, v2 = arr[i], arr[res - 1]

        # 찾은 용액 확인
        if i + 1 <= res < N and abs(arr[i] + arr[res]) < best_sum:
            best_sum = abs(arr[i] + arr[res])
            v1, v2 = arr[i], arr[res]

    print(v1, v2) # i 번째 용액을 확인할 때 i + 1번 용액부터 확인하기 때문에 항상 v1 <= v2 이다.


solution()