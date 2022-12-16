import sys
input = sys.stdin.readline
n,k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

start = min(levels)
# end = start +k
end = 1000000000
res = 0

while (start <= end):
    mid = (start + end)//2
    hap = 0
    for level in levels:
        if mid >= level:
            hap += (mid - level)
    if k >= hap: 
        res = mid
        start = mid +1#mid를 높이자 => hap이 증가함
    else: 
        end = mid -1 #올릴 수 있는 레벨보다 더 올렸다. mid를 낮추자 => hap이 감소함

    # if hap >= k:
    #     res=mid
    #     end = mid -1 
    # else:
    #     start = mid+1 
print(res)
