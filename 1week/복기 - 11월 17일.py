<의문사항을 정의>
    재귀를 돌때 반복이 되는 구간은 B구역 C구역이라고 파악하고 있는데
    왜? 문제 1074는 B구역이 한번만 C구역이 한번만 찍히지?
    너 말대로라면 4사분면 재귀 입장에서는 1~3사분이 전부 B구역에 해당하니까
    hi가 여러번 찍혀야하는거 아닌가? 
    마찬가지로 2사분 입자에서는 1,3,4가 C구역이니까 여러번 찍혀야하는거 아닌가?

    #B구역
        print("1"*n+"hi")
    #재귀구역
        recursion(n/2, r, c) #2사분
        recursion(n/2, r, c + (n/2)) #1사분
        recursion(n/2, r + (n/2), c) #3사분
        recursion(n/2, r+(n/2), c+(n/2)) #4사분
    #C구역
        print("1"*n+"bye")

<가설>
    #재귀구역 들어갈 때 재귀함수가 뭐예요?의
        recursion(count+1)과 

    #z의 이것이 차이가 나는 것 같은데
        recursion(n/2, r, c) #2사분
        recursion(n/2, r, c + (n/2)) #1사분
        recursion(n/2, r + (n/2), c) #3사분
        recursion(n/2, r+(n/2), c+(n/2)) #4사분
