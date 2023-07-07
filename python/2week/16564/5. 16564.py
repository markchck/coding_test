
# 3개 질문에 답을 해야함
# ===============================================================
# 1. min을 너무 작게 잡으면 mid를 min level보다 작게 잡아버릴 가능성이 생겨서 안되는건 알겠는데
#    max를 100000000000 처럼 그냥 대따 큰 값으로 잡는건 왜 안되나?
# => 결론부터 말하면 너의 가정이 맞다. 그냥 대따 큰 수를 집어 넣으면 이분탐색의 시간이 길어지긴하는데
# 그렇다고 답이 틀리지는 않는다. 단, 너의 코드는 지금 start~end-1까지만 탐색하는 코드라서 100000000을 탐색하게 하려면
# end= 10000000001까지 해주어야한다. (내 코드는 while(start<=end):)라서 왜 -1까지만 탐색중이라는 건지 추가 의문이 들어서 댓글로 물어본 상태임.
# ==============================================================
# 2. 왜 min+k가 max가 max이고 max(levels)+K//N가 max가 아니지?
# => 결론적으로 둘 다 상관없네 (어차피 답은 맞는다.) 
# ============================================================
# 3. 왜 위가 아니고 아래지?? (해결) 매우 중요!!!
#     # if hap >= k:
#     #     res = mid
#     #     end = mid-1
#     # else:
#     #     start = mid+1
        
#     if hap <= k:
#         start = mid+1
#         res = max(mid,res)
#     else:
#         end = mid -1

# 우리가 출력하는 res는 다른건 몰라도 이건 보장하는 res임 hap >= k (당연하지 if hap>=k 를 만족해야 res가 갱신되니까)
# 근데 우리가 원하는건 hap이 k를 넘지 않는 값을 원하는거지 넘어버리는 값을 원하는게 아니잖아? 
# 나무자르기랑은 다른게 나무자르기에선 hap >= k 즉, hap이 적어도 할당된 나무의 양 k를 넘어줬으면 했던거니까 res를 if hap >= k 에서 갱신한거고
# 히오스는 k를 넘지 않으면서 가장 높은 값을 원하니까 res 갱신을 if hap <= k: 여기서 해줘야한다. 그래야 다른건 몰라도 res가 k보단 작음을 보장 받지
# =========================================================



import sys
input = sys.stdin.readline
n,k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

start = min(levels)
# end = start +k
end = 1000000001
res = 0

while (start <= end):
    mid = (start + end)//2
    hap = 0
    for level in levels:
        if mid >= level:
            hap += (mid - level)
    if k >= hap: #mid가 낮다 올리자.
        res = mid
        start = mid +1
    else: #mid가 높다 낮추자
        end = mid -1
print(res)

