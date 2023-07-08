# 시간기준으로 sort
# 잠시멈춘과제를 넣는 배열 [과목, 잔여 시간] 넣고


def solution(plans):
    plans.sort(key=lambda x: x[1])
    for i, item in enumerate(plans):
        s_time, s_min = map(int, item[1].split(':'))
        item[1] = s_time*60 + s_min
        item[2] = int(item[2])
    # print(plans)
    # [['music', 740, 40], ['computer', 750, 100], ['science', 760, 50], ['history', 840, 30]]

    ptr = 0
    waiting = []
    result = []

    while plans:
        name = plans[ptr][0]
        time = plans[ptr][1]
        duration = plans[ptr][2]

        if ((ptr+1) <= len(plans)-1):
            next_name = plans[ptr+1][0]
            next_time = plans[ptr+1][1]
            next_duration = plans[ptr+1][2]
            if ((time+duration) > (next_time)): #중간에 멈춘 경우
                # 750-740만큼을 수행했으니까 40에서 빼줌
                waiting.append([name, duration - (next_time-time)])
                ptr = ptr+1
                
            else:
                result.append(name)
                plans = plans[0:ptr] + plans[ptr+1:]  #잘라내는 순간 기존의 배열의 인덱스와 바뀐 배열의 인덱스가 가리키는 놈이 달라져
                left_time = next_time - time+duration 
                if waiting:
                    plans[0][1]=next_time #pop을 쓰지 않으니까 인덱스 관리하기가 힘들어진다. 불가능은 아닌 것 같은데 복잡도가 너무 올라가버림. 
        else:
            


solution([["science", "12:40", "50"], ["music", "12:20", "40"], [
         "history", "14:00", "30"], ["computer", "12:30", "100"]])


# from datetime import datetime, timedelta
# def solution(plans):
#     # 시간기준으로 sort
#     plans.sort(key=lambda x: x[1])
#     for (i, item) in enumerate(plans):
#         name, begin, duration = item[0], item[1], item[2]
#         begin = datetime.strptime(begin, "%H:%M")
#         begin = begin.strftime("%H:%M")
#         duration = timedelta(minutes=int(duration))
#         end= begin+duration

#         # end와 다음 이터레이팅의 begin을 비교
