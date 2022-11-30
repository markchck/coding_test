#  개수정렬 복기
#      언제 쓰는가?
#         중복되는 놈들이 있는데 정렬을 해야할 때(n*log(n)정렬법으로는 안됨. 메모리 초과 뜸)
#      어케 쓰는가?
#         빈 배열을 먼저 만들고
#             a = [0]*100

#         1차원 배열 표현법으로 숫자들 넣고
#             배열의 순서 = 숫자 정보
#             배열의 값  = 개수 정보
#             ex) a[0] = 2는 1이 2개 있다는 소리

#         반복을 돌면서 개수에 맞게 출력 
#              if a[i] !=0 일때만 
#              i-1를 a[i]번 프린트

 리스트에 담았다가 셋 자료구조 변환 시키고 다시 리스트로 만들어서 중복 없애기
    
 sort와 람다함수로 조건 줘서 정렬하기 (key = lambda x : (len(x), x) )

 import sys
input = sys.stdin.readline

N = int(input())
word_list = []

for i in range(N):
    word = input().rstrip()
    word_list.append(word)

word_list = list(set(word_list))
print(word_list)

word_list.sort(key = lambda x : (len(x), x) )
for w in word_list:
    print(w)
