# 시간을 기준으로 이분탐색을 진행
def solution(n, times):
    answer = 0
    times.sort()
    left, right = 1, times[-1]*n
    people = 0
    while left <= right:
        mid = (left+right)//2
        for time in times:
            people += mid//time
            if people >= n:
                break
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
