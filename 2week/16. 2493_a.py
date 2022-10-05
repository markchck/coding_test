# https://www.acmicpc.net/problem/2493

# 내 바로 뒤에 있는놈이 나보다 키가 작으면 바로 0을 내뱉는게 아니라 그 뒤엣놈들도 탐색해야하는데 그걸 구현 못했음.
# 계속 for문에 for문에 for문으로 들어가는 것 밖에 생각나지 않음.. 중도 포기
# 이거 안되는거네.. 안된다기보다는 노가다임.
# 왜냐 내 바로 뒤에 있는 놈이 나보다 키가 작았어 그럼 그 뒤엣놈들을 대상으로 for문을 하나 새로 만들어서 크기를 비교해야지? 그러다가 나보다 키큰놈을 하나 만났어. for문은 종료되고 result에 값을 하나 추가했지?
# 그리고 for문을 새로 만드는 작업을 내 뒤엣놈이 나보다 키가 작을 때마다 반복해야함.
# 문제의 조건을 보면 N은 50만까지 들어올 수 있대. 최악의 경우(막대가 1부터 50만까지 오름차순으로 되어있다면?) for문 50만개 만들어야함.
# 재귀를 쓰면 코드의 양은 줄일 수 있을진 몰라도 재귀를 쓴다고 탐색을 덜하는건 아니니 50만*49만*48만*47만.....2번 만큼 데이터를 탐색하는 대참사가 발생할 수 있다.
# 결론 전혀 다른 접근법이 필요하다.


b1풀이와 내 풀이의 차이점을 생각해 보면서 든 생각임.(다음 명제는 참인가 생각해봐)
1. 배열을 하나 더 만드는게 시간을 줄여주는 건가?
2. 그럼 스택의 개념을 쓴게 시간을 줄여주는건가?
3. 난 b1풀이처럼 오른쪽부터 봐야겠다는 생각은 절대 못할 것 같은데 내풀이처럼 왼쪽부터보는 풀이는 왜 안되나?
4. 내 풀이중 result.appendleft(j+1)로 데이터를 왼쪽으로 삽입하는 로직이 있는데 이건 스택을 구현한건가?

답)
1. 아니. 2번과 연결되어있는데 한번에 설명할게. 만약 내가 오른쪽부터 보는걸 유지하고, b1풀이처럼 배열을 하나 더 만들었다고 생각해보자
먼저 4를 보겠지? 4는 뒤에있는 9가 더 크니까 result 배열에 들어갈거임.

그다음 7차례지? 7는 다음 5보다 키가 크니까 result배열에 들어가진 못하고 내가 만든 임의 배열에 넣어놓겟지? 왜? 더 왼쪽에 7보다 큰 놈이 나올지도 모르니까. 만약 나오면 그때 pop으로 빼줄거임.
그다음 5야. 5은 옆에가 9임. 9가 더 키가 크니까 result배열에 들어감.
그다음 9임. 9는 옆에가 6이니까 내가 더 커. 그래서 result배열엔 못들어감. 그리고 9는 임의배열에 쌓여있는 7을 보는거야. 9보다 7이 크니까 그제서야 7은 아 9한테 쏠 수 있겠네? 라고 생각하는거임. 그리고 7은 9를 쐇으면 됐었다고 기록하겠지.
그다음 6임 6은 옆에가 없으니까 패스.

이 방법이랑 b1풀이를 비교해보자.
임의배열에 6이들어가고 6은 내뒤에있는 9를 보겠지? 내 뒤가 더 크네? 9뒤에있는 놈들은 아무리 높은 놈이 와도 전부 9에 가려서 날 못맞출거임. 그래서 뒤에 전부 생각 안해도 됨.
따라서 임의배열에서 6을 빼버림. 다음 9가 임의배열에 들어감. 9는 뒤에있는 5를 보겠지? 나보다 키가 작네? 그럼 포인터 받을 수있다. result에 추가하고. 임의배열에는 9 유지해야함. 왜냐면 5이후에도 9보다 작은 놈들이 나올 수 있으니까.
그리고 5가 임의배열에 들어가고, 5는 뒤에있는 7을 보겠지? 나보다 키가 크네? 그럼 6처럼 뒤에 신경안써도 됨. pop으로 없애. 현재 임의배열에는 9가 아직 남음.
그다음 7이 임의배열에 들어가고 7은 뒤에있는 4를 보겠지? 나보다 작네? 그럼 포인터 받을 수 있고. 배열이 총 길이가 5니까 0~4범위를 넘어서 종료됨.

내 생각엔 내방법의 극단적인 경우는 오름차순(1,2,3,4~~)이고 / b1풀이의 극단적인 상황은 내림차순(10, 9, 8 ,7 ~~) 이라 최악의 상황에는 어차피 둘 다 끝까지 배열에 값을 가지고 있어야해서 둘은 무차별한 것 같다. (단, 구현이 누가 빡세느냐 문제인 듯?)
https://ywtechit.tistory.com/204 역기에 시간 복잡도 이야기가 나오는데.. 내말이 맞는거 같기도하고..?

2. 스택을 쓴다고 시간이 주는건 아닌듯한데?
https://ywtechit.tistory.com/204 참고

3. 된다.(구현이 어려울지는 모르겠음)

4. 큐냐, 스텍이냐는 데이터를 꺼낼때 먼저 쌓은놈을 꺼내느냐 나중에 쌓은 놈을 꺼내느냐 차이이지 쌓는거는 상관 없다.and
넌 왼쪽으로 쌓아서 스택이라 생각했는데, 그럼 오른쪽으로 갈수록 오래된 놈들이 있을거아니야? 근데 popleft해서 왼쪽을 꺼내버리면 그건 스택인거고 pop해서 오른쪽을 꺼내버리면 그건 큐인거고.pow
즉 꺼내는게 문제이지 쌓는건 상관없음.




import sys
from collections import deque
deq= deque
result=deque()

N=int(input())
# deq(map(int, sys.stdin.readline().split()))
deq=deq(map(int, sys.stdin.readline().split()))
count= 0
for i in range(len(deq)-1,-1,-1):
    for j in range(i-1,-1,-1):
        if i==j:
            pass
        else:
            if deq[i]<deq[j]: #뒤에 있는 타워가 키가 더 큰 더 뒤에있는 타워를 만나면..
                result.appendleft(j+1)
                break
            else:
                # 어떻게하면 바로 뒤엣놈 말고 더 뒤엣놈들 중 나보다 키 큰애가 있는지 추가 탐색을 하게 할 수 있을까? 바로 뒤엣놈만 보고 끝내는게 아니라.
                result.appendleft(0)
print(result)