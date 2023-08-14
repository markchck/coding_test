#  100000은 모든 경우의 수를 하기엔 너무 많다.
def solution(sticker):
    answer = 0
    if len(sticker) ==1:
        return sticker.pop()
    size = len(sticker)
    
    # sticker의 맨 처음 인자를 선택하는 경우 (맨 끝 인덱스는 선택 못하게 되기 때문에 [:-1])
    dp1 = [0] + sticker[:-1]
    for i in range(2, size):
        dp1[i] = max(dp1[i-1], dp1[i-2] +dp1[i])
    
    # sticker의 맨 끝 인자를 선택하는 경우 (0번 인덱스는 선택 못하기 때문에 [1:])
    dp2 = [0] +sticker[1:]
    for i in range(2, size):
        dp2[i] = max(dp2[i-1], dp2[i-2]+dp2[i])
    
    answer = max(dp1[-1], dp2[-1])
    print(answer)
    return answer

solution([1000, 10, 10, 2000, 30] 	)