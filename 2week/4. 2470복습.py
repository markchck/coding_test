import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

#그냥 하도 이진탐색 로직이 국밥이니까 심지어 함수로 뺄정도라는 거임. 별거없음
# idx, target만 무슨의미로 쓰인건지 아래 코드에서 확인하면 됨.
def binary_search(idx, target): 
    res = N-1
    start, end = idx, N-1

    while start <= end:
        mid = (start+end) //2
        if(arr[mid] >= target):
            res = mid
            end=mid-1
        else:
            start= mid+1
    return res

def solution():
    for i in range(N):
        res = binary_search(i+1, -arr[i])