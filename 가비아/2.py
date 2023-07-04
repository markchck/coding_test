# def solution(dots, lines):
#     lines.sort(reverse=True)
#     from collections import deque
#     que=deque((lines))
#     # dots=deque(dots)
#     length = len(que)
    
#     longest=que.popleft()
#     count = 0
#     ptr = 0
#     answer = []
#     while ptr <= len(dots)-1:
#         for i in range(ptr, len(dots)):
#             if( dots[ptr] + longest >= dots[i]):
#                 count+=1
#         answer.append([count,ptr])
#         count=0
#         ptr+=1
#     hi=max(answer)
        
        
    
    
#     return answer

# dots = [1,5,8]
# lines = [1,3,4,6]
# print(solution(dots, lines)) 


수평선 위에 점 여러 개가 놓여있는데 길이가 다양한 선분을 이용해 점들을 덮으려고해. 단 선분을 최소 개수만큼 사용해야해. 

def solution(dots, lines):
    answer = 0
    
    return answer

skeleton코드를 줄테니 위 조건을 만족하는 코드를 짜줘.

단 테스트 케이스 1, 2를 만족해야해
테스트케이스 1 : dots가 [1,5,8]이고 lines가 [1,3,4,6]인 경우 answer는 2
테스트케이스 2 : dots가 [1,3,4,6,7,10]이고  lines가 [2,2,2,2]인 경우 answer는 4

대답
주어진 문제는 수평선 위에 놓인 점들을 최소 개수의 선분으로 덮는 문제입니다. 이 문제는 그리디 알고리즘으로 해결할 수 있습니다.

그리디 알고리즘은 각 단계에서 최적의 선택을 하는 방식으로 문제를 해결합니다. 이 문제에서는 가장 왼쪽에 있는 점부터 시작하여 오른쪽으로 이동하면서 선분을 그리면서 최소 개수의 선분으로 모든 점을 덮을 수 있습니다.

따라서, 다음과 같이 구현할 수 있습니다.
여기서 i는 현재 선분으로 덮지 않은 가장 왼쪽의 점의 인덱스를 나타내고, j는 현재 선분으로 덮을 수 있는 가장 오른쪽의 점의 인덱스를 나타냅니다. j는 i부터 시작하여 현재 선분의 끝점 dots[i] + lines[-1]보다 오른쪽에 있는 가장 먼저 나타나는 점의 인덱스입니다. 이후 i를 j로 업데이트하고 다음 선분을 그립니다.

def solution(dots, lines):
    answer = 0
    i = 0 
    while i < len(dots):
        j = 0 
        while j < len(dots) and dots[i] + lines[-1] >= dots[j]:
            j += 1
        answer += 1 
        i = j 
    return answer



dots = [1,5,8]
lines = [1,3,4,6]
print(solution(dots, lines)) 