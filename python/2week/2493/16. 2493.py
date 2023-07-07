# 내방식대로라면 7이 6, 9, 5 n-1번 봐야함. n개의 인자가 있으니까 O(n^2)
# 위방식대로라면 7이 가장 큰 놈 9만 보면 됨. (9보다 작은 놈들은 pop으로 걸러졌거든) n개의 인자가 대빵하고만 보면 되니까 O(n)
# 내가 싸움 젤 잘하는거 증명하려고 모든 선수랑 붙어야하냐? 걍 챔피언만 이기면 되는거지

#정답풀이
#진행방향은 왼쪽에서 오른쪽으로 진행하고 예외상황(오른쪽이 왼쪽보다 키가 클때)발생시 더 키큰 애가 있는지 검증은 오른쪽에서 왼쪽으로 훑는 풀이.
#스택을 써서 오른쪽이 더 큰 경우 (=그림자에 가리는 놈들) Pop해주고 다음 예외 상황 발생시 그림자에 가리는 놈들은 보지 않고 가장 키큰 애와 바로 비교할 수 있게 함
import sys
input= sys.stdin.readline
N = int(input())
list_a = list(map(int, input().split()))
stack = []
result = [0]*N

for i in range(N):
    while stack:
        if list_a[stack[-1] -1] >= list_a[i]:
            result[i] = stack[-1] #(-1해야할 것 같지만 안하는 이유는 result에 들어가는건 인덱스가 아니라 순번이라서 1부터 시작함.)
            break
        else:
            stack.pop()
    stack.append(i+1)
print(*result)

# # 시도3) 진행방향은 왼쪽에서 오른쪽으로 진행하고 예외상황(오른쪽이 왼쪽보다 키가 클때)발생시 더 키큰 애가 있는지 검증은 오른쪽에서 왼쪽으로 훑는 풀이.
# # 정답풀이랑 차이는 스택을 따로 써서 오른쪽이 더 큰 경우 (=그림자에 가리는 놈들) Pop해주지 않고 그냥 for문 돌려서 전수조사함.
# import sys
# input = sys.stdin.readline

# N = int(input())
# list_a=list(map(int, input().split()))
# result = [0] * N

# for i in range(N):
#     if i < N-1:
#         if (list_a[i] > list_a[i+1]):
#             result[i+1] = i+1
#         else:
#             for j in range(i-1, -1, -1):
#                 if (list_a[j] > list_a[i+1]):
#                     result[i+1] = j+1
#                     break
#                 else:
#                     continue
# print(*result)


# # 시도2) 진행방향은 오른쪽에서 왼쪽으로 진행하고 예외상황(오른쪽이 왼쪽보다 키가 클때)발생시 더 키큰 애가 있는지 검증도 오른쪽에서 왼쪽으로 훑는 풀이 -> 시간복잡도 x
# import sys
# input = sys.stdin.readline
# N =int(input())
# list_a = list(map(int, input().split()))

# result = [0] * N

# while list_a:
#     idx=len(list_a)-1 # 몇번째 index를 기준으로 하는지
#     standard =list_a.pop()
#     if list_a: #왼쪽에 탑이 남아있으면?
#         # 왼쪽부터 보는게 아니라 오른쪽부터 봐야겠다.(시간복잡도)
#         for i in range(len(list_a)-1, -1, -1):
#             if list_a[i] >= standard:
#                 result[idx] = i+1
#                 break
# print(*result)



# # 시도1)진행방향은 오른쪽에서 왼쪽으로 진행하고 예외상황(오른쪽이 왼쪽보다 키가 클때)발생시 더 키큰 애가 있는지 검증은 왼쪽에서 오른쪽으로 훑는 풀이 -> 시간복잡도 x
# import sys
# input = sys.stdin.readline
# N =int(input())
# list_a = list(map(int, input().split()))
# # print(list_a)

# result = [0] * N

# while list_a:
#     idx=len(list_a)-1 # 몇번째 index를 기준으로 하는지
#     standard =list_a.pop()
#     if list_a: #왼쪽에 탑이 남아있으면?
#         for i in range(len(list_a)):
#             if list_a[i] >= standard:
#                 result[idx] = i+1
#             else:
#                 if result[idx] != 0:
#                     continue
#                 # else:
#                 #     result[idx] = 0
#     # else: #없으면? (0번 인덱스라면?)
#     #     result[0] = 0
# print(*result)