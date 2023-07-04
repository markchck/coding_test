# def solution(N, coffee_times):
#     length=len(coffee_times)
#     count = 0
#     answer = []
#     while len(answer) != length:
#         for i in range(length):
#             if coffee_times[i] !=0:
#                 if count < N:
#                     coffee_times[i] -=1
#                     count +=1
#             elif (coffee_times[i]==0 and (i+1 not in answer)): # 0이면
#                 answer.append(i+1)
#         count = 0
#     return answer

# print(solution(3, [4,2,2,5,3]))

N은 커피 추출구 개수이고, 각 커피를 만드는데 걸리는 시간이 주문번호 순서대로 담긴 배열 coffee_times가 있어.
커피가 완성되는 순서대로 주문 번호를 배열에 담아 return 하도록 solution 함수를 완성해야하고 아래 코드는 내가 작성한 정답코드야. 

def solution(N, coffee_times):
    length=len(coffee_times)
    count = 0
    answer = []
    while len(answer) != length:
        for i in range(length):
            if coffee_times[i] !=0:
                if count < N:
                    coffee_times[i] -=1
                    count +=1
            elif (coffee_times[i]==0 and (i+1 not in answer)): # 0이면
                answer.append(i+1)
        count = 0
    return answer


현재 1,2 번 테스트를 통과하는데 너가 시간 복잡도를 줄여줘.

1번 테스트 입력 : N=3, coffee_times = [4,2,2,5,5]
1번 테스트 answer : [2,3,1,5,4]

2번 테스트 입력 : N=1, coffee_times =[100,1,50,1,1]
2번 테스트 answer: [1,2,3,4,5]

단 너가 제시한 코드도 테스트 1, 2번은 통과해야해 

답변)
주어진 코드의 시간 복잡도는 O(N*M)입니다. 여기서 N은 커피 추출구의 개수이며, M은 주문한 커피의 수입니다. 이는 각 주문마다 모든 커피 추출구를 순회하며 가장 먼저 완성되는 커피를 찾는 방식으로 구현되어 있기 때문입니다.

이를 개선하기 위해서는 가장 먼저 완성되는 커피를 먼저 추출하도록 하는 방식으로 변경할 수 있습니다. 이를 위해 우선순위 큐(Priority Queue)를 사용합니다. 우선순위 큐는 데이터를 저장할 때 우선순위를 기준으로 저장하는 자료구조입니다. 여기서는 추출 시간이 가장 짧은 커피를 우선 추출하도록 하면 됩니다.

Python에서는 heapq 모듈을 이용하여 우선순위 큐를 구현할 수 있습니다. heapq 모듈은 이진 트리(binary tree)를 기반으로 하며, 최소 힙(min heap)으로 구현되어 있습니다.

따라서 우선순위 큐를 이용한 개선된 코드는 다음과 같습니다.

import heapq

def solution(N, coffee_times):
    answer = []
    pq = []
    end_time = 0
    for i, time in enumerate(coffee_times):
        if len(pq) < N:
            heapq.heappush(pq, (end_time + time, i+1))
        else:
            end_time, idx = heapq.heappop(pq)
            answer.append(idx)
            heapq.heappush(pq, (end_time + time, i+1))
    
    while pq:
        end_time, idx = heapq.heappop(pq)
        answer.append(idx)
        
    return answer
print(solution(3, [4,2,2,5,3]))
