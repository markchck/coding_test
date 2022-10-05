# https://www.acmicpc.net/problem/2493


if __name__ == "__main__":
    N = int(input())  # 탑의 개수
    top_list = list(map(int, input().split()))  # 탑 리스트
    stack = []
    answer = []

    for i in range(N):
        while stack: #스택에 뭔가가 있어서 비교할게 있으면 while이 돌 수 있는 상황인거..
            if stack[-1][1] > top_list[i]:  # 수신 가능한 상황  (스택에 쌓여있는 (과거)의 탑과 현재 보고있는 탑을 비교 중임.)
                answer.append(stack[-1][0] + 1)
                break
            else:
                stack.pop() 
                #6뒤에 9가 더 크니까 더이상 6을 스택에 가지고 있을 필요가 없음. (왜냐 9뒤에 뭐가 오더라도 9에 가려서 안보일테니 비교할 필요가 없다.)
                #5와 비교가 끝난 후에도 9는 pop을 하지 않는다. 왜? 뒤에 키가 더 낮은 놈이 오면 또 9에 쏠 수 있으니까. 타임머신처럼 과거를 저장하고있는 스택에서 9를 한번 비교했다고 없애버리면 뒤에 비교가 안되자너
        if not stack:  # 스택이 비면 레이저를 수신할 탑이 없다.
            answer.append(0)
        stack.append([i, top_list[i]])  # 스택은 과거의 탑을 지금 보는 탑과 비교하기 위해 저장해놓는 용도군!(지금보는 탑을 스택에 넣어놔야 다음 탑과 비교할 수 있는거지.)

    print(" ".join(map(str, answer)))