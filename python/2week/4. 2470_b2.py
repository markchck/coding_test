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

    # 1. 왜 binary_search(i + 1, -arr[i])인가?
        # 이분 탐색 수행: 현재 위치(i)가 i라면 i 오른쪽의 용액(i+1)을 탐색하고
        # 찾아야하는 값은 (현재 용액 * -1)과 근사한 값이다. 
        # 예를 들어 i번째(3번째) 숫자가 -99라고하면 i+1번째(4번째) 숫자부터 배열의 끝인 n-1번째 숫자까지 뒤지는데 
        # 찾는 숫자는 -(-99) 즉 99를 찾는다는 소리이다. 그래야 우리의 목표인 합쳐서 0이 되는 용액을 찾는거니까
        # 우리는 정렬을 이미 했기 때문에 i보다 왼쪽에 있는 숫자들(0,1,2)은 안봐도 됨 i가 -99면
        # 걔네들은 -120, -110 이라 더하면 0에 가까워지는게 아니라 더 멀어지는 놈들이니까
        res = binary_search(i + 1, -arr[i])
    
    # 2. 여긴 뭐하는 곳인가?
        # binary_search로 찾은 res번째 값이 99랑 가장 가까운 값이 아닐 수 있다. 
        # 하나 보장할 수 있는거는 res오른쪽의 값이 res보다 99랑 가까울 수는 없다는 것 이진탐색 시 (if(arr[mid] >= target):) 이 조건 들어갈 때 res = mid해놓고 들어가기 때문에.. 
        # 그러나 res왼쪽 값이 99랑 가까울 수 없다는 건 보장 못함. 그래서 res -1번 째 값이 혹시 더 99에 가까운지 봐야함.
        

        # 찾은 용액의 바로 왼쪽 용액 확인
        # i+1<= res-1 < N 먼저 보면 이 조건은 res-1을 했는데 i보다 왼쪽의 숫자인 -120, -110인 경우를 없게하려고
        # abs(arr[i] + arr[res - 1]) < best_sum 여기서 best_sum이 등장한 이유는?
            # 결론부터 말하면 메모리를 절약하려고 최댓값, 최솟값 구할 때 이렇게 엄청 큰 수, 엄청 작은 변수를 설정해놓고 반복문을 돌면서 더 작은 값, 더 큰 값이 등장하면 변수를 갱신하면서 반복문을 돌다가 마지막에 그 변수를 print하는 로직이 많이 들어간다.
            # 너라면 아마 abs(arr[i] + arr[res - 1]) 값들을 전부 어떤 배열 x를 하나 새로 선언해서 다 append시켜놓고 최종적으로 print( min(x) ) 이런 식으로 답을 구했겠지. 
            # 물론 틀린거는 아님. 메모리랑 시간이 더 들어갈 뿐..
            # 아무튼 best_sum이 무한대였다가 abs(arr[i] + arr[res - 1]) 이렇게 갱신된 채로(작아진채로, 5가 되었다고 치자) 다음 루프가 돌고
            # 다음 루프는 5보다 작은 3,4 같은 애들이여야만 print(v1,v2)될 수 있는거임.
        
        if i + 1 <= res - 1 < N and abs(arr[i] + arr[res - 1]) < best_sum:  
            best_sum = abs(arr[i] + arr[res - 1])
            v1, v2 = arr[i], arr[res - 1]

        # 찾은 용액 확인
        # 위에서 res 왼쪽을 봐서 best_sum값이 낮춰져있었겠지? 5라고 치자
        # 그럼 이제 res 너를 보는거야. abs(arr[i] + arr[res]) 이게 5보다 작아야만 v1, v2 를 갱신할 수 있다.
        if i + 1 <= res < N and abs(arr[i] + arr[res]) < best_sum:
            best_sum = abs(arr[i] + arr[res])
            v1, v2 = arr[i], arr[res]

    print(v1, v2) 

    # 솔직히.. 왜 왼쪽도 봐야하는지, 왜 찾은 용액 확인이 찾은 용액 왼쪽 확인보다 뒤에 와야만 하는건지 잘 모르겠다..


solution()


# 이 풀이 그럴듯한데 틀림... 왠지는 모르겠음..
# import sys
# input = sys.stdin.readline


# N = int(input())
# arr = sorted(list(map(int, input().split())))

# def binary_search(idx, target):
#     res = N-1
#     start, end = idx, N - 1
#     while start <= end:
#         mid = (start+end) //2
#         if(arr[mid] >= target): #이렇게 써도 통과~
#             res = mid
#             end=mid-1
#         else:
#             start= mid+1
#     return res


# def solution():
#     # v1, v2 = 0, 0
#     # best_sum = 10 ** 10
#     sample=[]
#     for i in range(N):
#         res = binary_search(i + 1, -arr[i])
#         sample.append((arr[i], arr[res], arr[i]+arr[res]))
    
#     sorted(sample, key = lambda x : x[2])
#     print(sample[0][0], sample[0][1])

# solution()