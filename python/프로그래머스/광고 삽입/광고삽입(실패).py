# 1초 2초....전부 다 광고 시작시간으로 해보면 되지만
# 그리디한 관점에서 다 해볼 필요 없이 logs 각각의 시작 시간 중 하나에 광고를 틀면 된다.
# logs의 모드 합과 광고 시간의 합을 비교해서 광고시간이 더 크면 (예제 3번과 같은 예외 케이스간됨.)
def solution(play_time, adv_time, logs):
    items = []
    for log in logs:
        start_log, end_log = log.split('-')
        s_time, s_min, s_sec = map(int, start_log.split(":"))
        e_time, e_min, e_sec = map(int, end_log.split(":"))
        items.append([s_time*3600+s_min*60+s_sec, e_time*3600+e_min*60+e_sec])
    items.sort(key=lambda x: (x[0]))

    ad_t, ad_m, ad_s = map(int, adv_time.split(":"))
    ad_time = ad_t*3600+ad_m*60+ad_s
    # print(items)

    sum = 0
    ad_start = 0
    for idx, item in enumerate(items):
        start = item[0]
        end = item[1]
        ad_start = start
        ad_end = start + ad_time
        if ad_end >= end:
            sum += (end-ad_start)
            ad_start = end
            ad_time = ad_time - (end-ad_start)


solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00",
         "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
