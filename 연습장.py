def solution(sticker):
    answer = 0
    size= len(sticker)
    if(size == 1):
        return sticker.pop()
    dp1 = [0] + sticker[:-1]
    for i in range(2, size):
        dp1[i] = max(dp1[i]+dp1[i-2], dp1[i-1])
    
    dp2 = [0] + sticker[1:]
    for i in range(2, size):
        dp2[i] = max(dp2[i]+dp2[i-2], dp2[i-1])
    
    answer = max(dp1[-1], dp2[-1])
    return answer