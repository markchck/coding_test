# 시간관리를 편하게하기 위해서 전부 분으로 바꾼다.
# sort를 사용해서 시작시간 순서대로 정렬한다.
# 인덱스 관리를 편하게 하기 위해서 pop하는 것을 고려.
# i, i+1, i+2도 봐야함. (i의 작업이 끝난 경우 i+1과 i+2를 봐야하기 때문에..)

def solution(plans):
    # 분으로 바꾼다.
    for plan in plans:
        time, min = map(int, plan[1].split(":"))
        time = time * 60
        plan[1] = time+min
        plan[2] = int(plan[2])

    # 시작시간 기준으로 정렬한다.
    # [['korean', 700, 30], ['english', 730, 20], ['math', 750, 40]]
    plans.sort(key=lambda x: x[1])
    waiting = []
    answer = []

    # 가장 먼저 시작하는 것을 pop해서 볼거야.
    while plans:
        # plans에 최소 2개는 있어야 함.
        if (len(plans) >= 2):
            name, start, duration = plans[0]
            plans = plans[1:]
            nStart = plans[0][1]
            if (start+duration > nStart):  # 다음 과목 전에 한 과목을 못 끝낸 경우
                # 대기열에 넣어줘야함. 단 수행한 시간만큼은 빼준 상태로 넣어야함
                waiting.append([name, start + duration - nStart])
            else:  # 끝낸 경우
                # 결과 배열에 넣어줘야함.
                answer.append(name)
                # 대기열에 가장 최근에 들어간걸(맨 뒤) plans의 맨 앞으로 넣어주면 됨
                if (waiting):
                    wName, wDuration = waiting.pop()
                    plans = [[wName, start+duration, wDuration]] + plans
        else:  # 하나 남은 경우는 waiting만 확인하고 없으면 그냥 출력하면 됨. 0인 경우는 while문이 종료되니 볼 필요 없고
            name, start, duration = plans.pop()
            if (waiting):
                wName, wDuration = waiting.pop()
                plans = [[wName, start+duration, wDuration]] + plans
            answer.append(name)
    return answer


# solution([["science", "12:40", "50"], ["music", "12:20", "40"], [
#          "history", "14:00", "30"], ["computer", "12:30", "100"]])
