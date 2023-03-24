# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())

# result = []
# for i in range(1, N+1):
#     result.append(i)

# answer=[]
# while len(result)!=0:
#     left=len(result)
#     if left >= K:
#         pop=result[K-1]
#         answer.append(pop)
#         result = result[:(left-1)] + result[left:]
#     else:
#         pop=result[left%K -1]
    
# print(answer)

