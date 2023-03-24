16564 히오스

mid값까지는 나무자르기랑 비슷한 생각이었다.
하나 특이한 건 max값을 구하는 거였는데

min값 + K가 max라는 것이다.
나는 min + K//N이라고 생각했다.

3개 질문에 답을 해야함
1. 둘 중 max값이 뭐든 이분 탐색 하는데에는 영향이 없을 거라 생각했는데 아니네? 왜 end값이 mid에 영향?
2. 왜 min+k가 max가 max이고 min+K//N은 아니지?
3. 왜 위가 아니고 아래지??
    # if hap >= k:
    #     res = mid
    #     end = mid-1
    # else:
    #     start = mid+1
        

    if hap <= k:
        start = mid+1
        res = max(mid,res)
    else:
        end = mid -1