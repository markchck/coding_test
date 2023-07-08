from collections import deque


def solution(plans):
    plans.sort(key=lambda x: x[1])
    que = deque()
    for plan in plans:
        time, min = map(int, plan[1].split(':'))
        plan[1] = time*60 + min
        plan[2] = int(plan[2])
        que.append([plan[0], plan[1], plan[2]])

    waiting = []
    result = []
    while que:
        if len(que) >= 2:
            cName, cTime, cDuration = que.popleft()
            nName, nTime, nDuration = que[0]
            if (cTime + cDuration > nTime):
                leftDuration = cDuration - (nTime-cTime)
                waiting.append([cName, leftDuration])
            else:
                result.append(cName)
                if (waiting):
                    wName, wDuration = waiting.pop()
                    que.appendleft([wName, cTime+cDuration, wDuration])
        else:
            cName, cTime, cDuration = que.popleft()
            if (waiting):
                wName, wDuration = waiting.pop()
                que.appendleft([wName, cTime+cDuration, wDuration])
            result.append(cName)
    return result


solution([["science", "12:40", "50"], ["music", "12:20", "40"], [
         "history", "14:00", "30"], ["computer", "12:30", "100"]])
