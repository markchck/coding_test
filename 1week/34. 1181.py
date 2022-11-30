# https://www.acmicpc.net/problem/1181
# 개수정렬 아이디어를 변형해서 일단 서류들 넣을 빈 상자들 쭉 만들고
# 단 2차원으로. 왜냐 단어도 들어가고 단어의 길이 정보도 담아야해서
# 만들 때는 set를 활용(중복된거 알아서 제거)

# 프린트할 때는 for 문 돌면서 
# if문으로 길이가 1개뿐인놈 (= {0}만 잇는 놈) 제끼고
# 살아남은 놈들 2번재 인자부터 끝인자까지 쭉 출력할 생각이엇음.
# [{0, 'i'}, {0, 'it', 'no', 'im'}, {0, 'but'}, {0, 'wont', 'more', 'wait'}, {0, 'yours'}, {0, 'cannot'}, {0}, {0, 'hesitate'}]


# <미완성 풀이 - 하다가 시간 부족해서 문제 외우기로 넘어감>
import sys
input = sys.stdin.readline

# list_l = [0]*100
list_l = ([{0} for _ in range(200)])

for i in range(int(input())):
    text = input().rstrip()
    text_len = len(text)
    list_l[len(text)-1].add(text)
    
for j in range(200):
    if len(list_l[j] != 1):
        for k in range(len(list_l[j])):
            pass
# print(list_l)