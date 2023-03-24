import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    M = input().strip().split(' ')
    scores  = list(map(float, M[1:]))
    average = sum(scores)/len(scores)

    above = 0
    for score in scores:
        if score > average:
            above += 1
    # print(f'{(above/len(scores)*100):.3f}%')
    #  :의 의미는 변수 타입 주석 (.3f를 타입으로 가져라라는 의미)
    #  ->의 의미는 함수 타입 주석

    output = format((above/len(scores)*100), '.3f')
    print('%s%%' %(output))





# # 각 케이스를 배열로 받고(배열에 넣을 필요 없네!!) SUM 함수를 써서 배열의 합을 구한다.
# # 단 맨 앞 숫자는 제외해야하는데 이게 뽀인트인듯

# # SUM한 값을 학생수로 나눠서 평균을 구하고 
# # 배열을 FOR문 돌면서 평균 보다 큰 학생을 카운트 변수에 넣는다. 

# # PRINT 카운트 변수 / 학생수로 정답 비율을 출력하는데
# # 소수점 셋째짜리까지니까 어떤 문법을 써야할 것 같은데 모르겠음.

# import sys
# input = sys.stdin.readline

# N = int(input())
# for i in range(N):
#   M = map(int, input().split())
#   student_n = M[0]
#   scores = M[1:]
#   sum_scores = sum(scores)
#   average = sum_scores/student_n

#   for score in scores:
#     count = 0
#     if score>average:
#       count +=1
#     above_average_rate = count/student_n
#   print(above_average_rate)  