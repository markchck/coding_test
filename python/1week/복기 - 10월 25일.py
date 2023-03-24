# 오늘 외운거
# 1. 소숫점 3째자리까지 출력하기
    # print(f'{0.123344*100:.3f}%')
# 2. ox퀴즈 문제 풀기 (굳이 배열에 넣지 않고 풀 수 있구나!)
# 3. 좋은 풀이 찾는 방법 (백준 고고)

A = int(input())

for i in range(A):
    M = input()
    seq=0
    sum=0
    for i in range(len(M)):
        if M[i] == "O":
            seq =+1
            sum =+seq
        else:
            seq=0
    print(sum)
